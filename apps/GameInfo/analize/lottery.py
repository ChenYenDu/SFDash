"""
此檔案為開獎分析 API 專用
API 命名規則 LotteryViewSet[彩類], e.g. PK開獎分析: LotteryViewSetPK

API for lottery number analize
Naming Rule: GameLotteryViewSet{GameType}
"""

import datetime
import pandas as pd
import numpy as np

from django.db.models import Count, F, Q, Subquery, Sum
from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.GameInfo.models import GameBuylist, GameKinds, GameLottery, GameType
from apps.GameInfo.pagination import StandardResultSetPagination

class LotteryAnaBase(ListAPIView):
    """
    開獎分析用基礎架構, 其他其他
    """
    queryset = GameLottery.objects.using('bo2')

    def validate(self, date_text):
        try:
            if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            # raise ValueError("錯誤日期格式, 格式是 yyy-mm-dd")
            return False
    
    def get_data(self, start_date, end_date, playkey, cols=['number', 'period']):
        """
        從資料庫抓取時間區間內該playkey的資料欄位[cols]
        """
        result = {}

        # 這裡使用 Django ORM 原生操作
        # 也可以使用 pymysql cursor 取得資料
        lottery = self.queryset.filter(
            Q(lottime__range=(start_date, end_date)) &
            Q(playkey = playkey) &
            Q(status__in=(0, 1))) \
                .values(*cols) \
                    .order_by(F('lottime').desc())

        # 轉換成 pandas DataFrame 之前確認資料庫取得資料正常
        if not lottery.exist():
            result['error_code'] = 1
            result['message'] = '選取條件查無資料'
            return result
        
        # 轉換成 pandas DataFrame,
        # 經過判斷 遺漏值 多為操作錯誤資料，可直接移除
        df = pd.DataFrame.from_records(lottery)
        df = df.dropna(axis=0, how='any')

        # 用戶需求： 回傳最新 period
        result['period'] = df['period'].values[0]
        result['df'] = df

        return result

    def data_manipulate(self, df):
        # 資料分析流程放在這裡
        result = {}
        return result
    
    def get(self, request):
        
        # 取得 request parameters: StartDate, EndDate, Playkey
        todate = datetime.date.today().strftime('%Y-%m-%d')

        StartDate = request.query_params.get('StartDate', todate)
        EndDate = request.query_params.get('EndDate', todate)
        Playkey = request.query_params.get('Playkey', 'WNPK_p')

        response = {
            'StartDate': StartDate,
            'EndDate': EndDate,
            'Playkey': Playkey,
        }

        # 檢查開始日期格式
        if self.validate(StartDate):
            StartDate = datetime.datetime \
                .strptime(
                    StartDate + " 00:00:01", "%Y-%m-%d %H:%M:%S"
                )
        else:
            response['error_code'] = 2
            response['message'] = '開始日期格式錯誤'
            return JsonResponse(response, safe=False)
        
        # 檢查結束日期格式
        if self.validate(EndDate):
            EndDate = datetime.datetime \
                .strptime(
                    EndDate + " 23:59:59", "%Y-%m-%d %H:%M:%S"
                )
        else:
            response['error_code'] = 2
            response['message'] = '結束日期格是錯誤'
            return JsonResponse(response, safe=False)

        # 如果格式都沒問題 StartDate 和 EndDate 格式已經是 datetime
        # 確認日期順序避免資料庫抓不到資料
        if EndDate > StartDate:
            StartDate, EndDate = EndDate, StartDate # 直接互換, 或回傳error
        
        # 取得分析用資料
        Playkey = Playkey.replace('_p', '')
        df_info = self.get_data()

        # 取回 df_info 之後先判斷 error_code 是否為 0
        if df_info['error_code']: # error_code 不為 0 直接回傳
            response.update(df_info)
            return JsonResponse(response, safe=False)
        else: # error_code 為 0 繼續分析
            df = df_info.pop('df')
            response['period'] = df_info['period']
            
            result = self.data_manipulate(df)

            response.update(result)
            return Response(response)
    
    def getSNO(self, target, col):
        """
        計算連續未開出次數
        target: 判斷的目標
        col: 計算的欄位
        """
        result = dict(zip(target, [0] * len(target)))
        colLen = len(col)

        # 避免使用for去計算連續未出現次數,
        # 直接用 pandas loc 找到第一個符合的index
        for ts in target:
            ff = col.loc[col.apply(lambda ele: ts in ele)]
            result[ts] = ff.index[0] if len(ff) > 0 else colLen

        return temp
    
    def getSSO(self, target, col):
        """
        計算連續開出次數
        target: 判斷的目標
        col: 計算的欄位
        """
        result = dict(zip(target, [0] * len(target)))

        for ts in target:
            result[ts] = col.loc[col.apply(lambda ele: ts not in ele)].index[0]

        return result
        

class LotteryViewSetPK(LotteryAnaBase):
    """
    PK類開獎分析API:
    1. **ranks** 各名次開獎資料
        - __ballCount__:  &#8194 球號： 累積開出次數
        - __ballSNO__: &#8194 球號： 連續未開次數
        - __dsCount__: &#8194 大小： 累積開出次數
        - __dsSNO__: &#8194 大小： 連續未開出次數
        - __ejCount__: &#8194 單雙： 累積開出次數
        - __ejSNO__: &#8194 單雙： 連續未開出次數
        - __lhCount__: &#8194 龍虎： 累積開出次數
        - __lhSNO__: &#8194 龍虎： 連續未開出次數
    2. **csPairCount:** &#8194 冠亞組合 累積開出次數
    3. **csDSCount:** &#8194 冠亞和值 **大小** 累積開出次數
    4. **csEJCount:** &#8194 冠亞和值 **單雙** 累積開出次數
    5. **csTotalCount:** &#8194 冠亞和值 **和值** 累積開出次數
    """

    def data_manipulate(self, df):
        super().data_manipulate(df)
        result = {}
        
        # 建立拆解後的欄位名稱：名次
        ranks = [
            "NO1", "NO2", "NO3", "NO4", "NO5",
            "NO6", "NO7", "NO8", "NO9", "NO10"
        ]

        # split number to each columns
        df[ranks] = df.number.str.split(',', n=10, expand=True)
        del df['number'] # number is no longer used, free memory

        # 計算每個名次 每一車 累積開出次數
        count_df = df[ranks].apply(pd.value_counts)
        
        # 創建從 01 ~ 10 的車號
        cars = [str(ele).zfill(2) for ele in range(1, 11)]

        # 計算每個名次 每一車 連續為開出次數
        sno = pd.DataFrame([
            self.getSNO(cars, col=df[col]) for col in ranks
        ], index=ranks).T

        # 先把需要用到的資料轉成 dictionary
        rankCount = count_df.to_dict()
        rankSNO = sno_df.to_dict()

        # 計算 大小/單雙 累積開出次數
        count_df = count_df.rename_axis('cars').reset_index()
        count_df['cars'] = count_df['cars'].astype('int')

        # 建立 大小/單雙 的欄位
        count_df['DS'] = count_df['cars'] \
            .apply(lambda ele: 'D' if ele > 5 else 'S')
        count_df['EJ'] = count_df['cars'] \
            .apply(lambda ele: 'J' if ele % 2 else 'E')
        
        ds_count = count_df.groupby('DS')[ranks] \ 
            .sum().to_dict() 
        ej_count = count_df.groupby('EJ')[ranks] \
            .sum().to_dict()
            
        # 計算 大小/單雙 連續未開出次數
        sno = sno.rename_axis('cars').reset_index()
        sno['cars'] = sno['cars'].astype('int')
        sno['DS'] = sno['cars'].apply(lambda ele: 'D' if ele > 5 else 'S')
        sno['EJ'] = sno['cars'].apply(lambda ele: 'J' if ele % 2 else 'E')
        ds_sno = sno.groupby('DS')[ranks].min().to_dict()
        ej_son = sno.groupby('EJ')[ranks].min().to_dict()
        
        # 計算 冠亞組合 累積開出次數
        cs_pair = df.groupby(ranks[:2])['period'].size().reset_index()

        # 計算 龍虎 累積開出次數
        df[ranks] = df[ranks].apply(pd.to_numeric, errors="coerce")
        
        lh_columns = ['LH1', 'LH2', 'LH3', 'LH4', 'LH5']

        df = df.assign(
            LH1=df['NO1'] > df['NO10'],
            LH2=df['NO2'] > df['NO9'],
            LH3=df['NO3'] > df['NO8'],
            LH4=df['NO4'] > df['NO7'],
            LH5=df['NO5'] > df['NO6'],
        )

        df[lh_columns] = np.where(lh_columns, 'L', 'H')

        lh_count = df[lh_count].apply(pd.value_counts).to_dict()

        # 計算 龍虎 連續未開出次數
        lh_sno = pd.DataFrame(
            [self.getSNO(target=['L', 'H'], col=df[col]) for col in lh_columns],
            index=ranks[:5]
        ).to_dict('index')

        # 計算 冠亞和值 累積開出次數
        df['CS_Total'] = df['NO1'] + df['NO2']
        cs_total_count = df.groupby('CS_Total')['period'] \
            .size().reset_index()

        # 計算 冠亞和值 大小、單雙累積開出次數
        cs_total_count['DS'] = cs_total_count['CS_Total'] \
            .apply(lambda ele: 'H' if ele == 11 else 'D' if ele > 11 else 'S')

        cs_total_count['EJ'] = cs_total_count['CS_Total'] \
            .apply(lambda ele: 'H' if ele == 11 else 'J' if ele % 2 else 'E')
        
        cs_ds_count = cs_total_count.groupby('DS')['period'].sum().to_dict()
        cs_ej_count = cs_total_count.groupby('EJ')['period'].sum().to_dict()

        # 重新架構回傳的資料
        result['CS_Total_Count'] = cs_total_count[['CS_Total', 'count']].to_dict('records')
        result['CS_DS_Count'] = cs_ds_count
        result['CS_EJ_Count'] = cs_ej_count
        
        result['Rank_Count'] = rankCount
        result['Rank_SNO'] = rankSNO
        result['DS_Count'] = ds_count
        result['EJ_Count'] = ej_count
        result['DS_SNO'] = ds_sno
        result['EJ_SNO'] = ej_son
        return result