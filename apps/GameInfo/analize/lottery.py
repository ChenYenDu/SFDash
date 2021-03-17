"""
此檔案為開獎分析 API 專用
API 命名規則 LotteryViewSet[彩類], e.g. PK開獎分析: LotteryViewSetPK

API for lottery number analize
Naming Rule: GameLotteryViewSet{GameType}
"""

import datetime
import pandas as pd

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
    
    def get_data(start_date, end_date, playkey, cols=['number', 'period']):
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
            df = df_info.pop('df')
            response['period'] = df_info['period']
            
            result = self.data_manipulate(df)

            response.update(result)
            return Response(response)
        

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
        
        # 建立拆解後的欄位名稱
        columns = [
            "NO1", "NO2", "NO3", "NO4", "NO5",
            "NO6", "NO7", "NO8", "NO9", "NO10"
        ]

        # split number to each columns
        df[columns] = df.number.str.split(',', n=10, expand=True)
        del df['number'] # number is no longer used, free memory

        # 計算每個名次 每個球 累積開出次數

        return result