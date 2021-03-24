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

from apps.GameInfo.models import GameBuylist, GameLottery
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
            response['error_code'] = 0
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

        resultCollect = {}
        for rank in rank_name:
            tempRecord = {}
            tempRecord['Ball_Count'] = rankCount[rank]
            tempRecord['Ball_SNO'] = rankSNO[rank]
            tempRecord['DS_Count'] = DSCount[rank]
            tempRecord['EJ_Count'] = EJCount[rank]
            tempRecord['DE_SNO'] = DSSNO[rank]
            tempRecord['EJ_SNO'] = EJSNO[rank]

            if rank in rank_name[:5]:
                tempRecord['LH_Count'] = LHCount[rank]
                tempRecord['LH_SNO'] = LHSNO[rank]

            resultCollect[rank] = tempRecord

        result['ranks'] = resultCollect
        return result

class GameLotteryViewSetSSC(LotteryAnaBase):
   """
    代碼: A1 -> 萬 | A2 -> 千 | A3 -> 百 | A4 -> 十 | A5 -> 個

    1. ** ballCount: ** &#8194 每個位置每一號 累積開出次數
    2. ** ballSNO: ** &#8194 每個位置每一號 連續「未開出」次數
    3. ** ballSSO: ** &#8194 每個位置每一號  連續「開出」次數
    4. ** twoStar: ** &#8194 二星 累積開出次數 (前20)
    5. ** threeStar: ** &#8194 三星 累積開出次數 (前20)
    6. ** fourStar: ** &#8194 四星 累積開次數 (僅 五星|四星彩 提供) (前20)
    7. ** dsSSO: ** &#8194 大小 連續開出次數
    8. ** dsSNO: ** &#8194 大小 連續未開出次數
    9. ** ejSSO: ** &#8194 單雙 連續開出次數
    10. ** ejSNO: ** &#8194 單雙 連續未開出次數
    """

    def data_manipulate(self, df):
        super().data_manipulate(df)
        result = {}

        # 3, 4星彩判斷
        starDict = {
            'threeStar': ['D3SSC', 'P3SSC', 'SHSSC', 'TWD3SSC'],
            'fourStar': ['TWD4SSC', 'LAOD4SSC', 'DMCD4SSC', 'TOTOD4SSC', 'MND4SSC', 'SGCD4SSC'],
        }

        # 判斷 Playkey 是幾星彩
        if Playkey in starDict['threeStar']:
            mask = df['number'].str.len() == 5
            df = df.loc[mask]
            positions = ['A3', 'A4', 'A5']
            df[positions] = df.number.str \
                .split(',', n=len(positions), expand=True)
            result['stars'] = 3
        elif Playkey in starDict['fourStar']:
            mask = df['number'].str.len() == 7
            df = df.loc[mask]
            positions = ['A2', 'A3', 'A4', 'A5']
            df[positions] = df.number.str \
                .split(',', n=len(positions), expand=True)
            result['stars'] = 4
        else:
            mask = df['number'].str.len() == 9
            df = df.loc[mask]
            positions = ['A1', 'A2', 'A3', 'A4', 'A5']
            df[positions] = df.number.str \
                .split(',', n=len(positions), expand=True)
            result['stars'] = 5

        # 所有球號
        balls = [str(ele) for ele in range(10)]
        numCand = pd.DataFrame({'ball': balls})
        numCand['DS'] = numCand['ball'].astype(int).apply(
            lambda ele: 'D' if ele > 4 else 'S')
        numCand['EJ'] = numCand['ball'].astype(int).apply(
            lambda ele: 'J' if ele % 2 else 'E')

        # 各球位統計累積開出次數
        ballCount = df[positions] \
            .apply(pd.value_counts).rename_axis(index='ball') \
            .reset_index()

        ballCount = pd.merge(numCand, ballCount, how='outer') \
            .fillna(0).set_index('ball')

        result['ballCount'] = ballCount[positions].to_dict()

        # 計算每個位置 每顆球的連續開出|連續未開出
        SSO = {}
        SNO = {}
        for col in positions:
            SSO[col] = pd.Series(self.getSSO(balls, df[col])).to_dict()
            SNO[col] = pd.Series(self.getSNO(balls, df[col])).to_dict()

        result['ballSNO'] = SNO
        result['ballSSO'] = SSO

        # 計算 每個位置 大小 累積開出次數
        # 單碼 大小累積開出次數 ( 正碼 1~6 )
        ballDSCount = ballCount.groupby('DS')[positions].sum().to_dict()
        result['ballDSCount'] = ballDSCount

        # 計算 每個位置 單雙 累積開出次數
        ballEJCount = ballCount.groupby('EJ')[positions].sum().to_dict()
        result['ballEJCount'] = ballEJCount

        # 計算 二星　組合　累積開出次數
        result['twoStar'] = {}
        front2 = df.groupby(positions[:2])['period']\
            .size().reset_index()

        end2 = df.groupby(positions[-2:])['period'] \
            .size().reset_index()

        result['twoStar']['front2'] = front2.head(20).to_dict('records')
        result['twoStar']['end2'] = end2.head(20).to_dict('records')

        # 計算 三星 組合
        result['threeStar'] = {}

        front3 = df.groupby(positions[:3])['period'] \
            .size().reset_index()

        result['threeStar']['front3'] = front3.head(20).to_dict('records')

        if Playkey not in starDict['threeStar']:
            # 計算後三 只要不是三星彩種
            end3 = df.groupby(positions[-3:])['period'] \
                .size().reset_index()
            result['threeStar']['end3'] = end3.head(20).to_dict('records')

            # 計算四星 只要不是三星彩種
            fourStar = df.groupby(positions[-4:])['period'] \
                .size().reset_index()
            result['fourStar'] = fourStar.head(20).to_dict('records')

            # 只有五星彩種才要計算中三
            if Playkey not in starDict['fourStar']:
                middle3 = df.groupby(positions[1:-1])['period'] \
                    .size().reset_index()
                result['threeStar']['middle3'] = middle3.head(
                    20).to_dict('records')

        # 計算 大小單雙 連續開出次數
        dsSSO, dsSNO = {}, {}
        ejSSO, ejSNO = {}, {}
        for col in positions:
            dsSSO[col] = pd.Series(
                self.getSSO(['D', 'S'], df[col].astype(int).apply(
                    lambda ele: 'D' if ele > 4 else 'S'))
            ).to_dict()

            dsSNO[col] = pd.Series(
                self.getSNO(['D', 'S'], df[col].astype(int).apply(
                    lambda ele: 'D' if ele > 4 else 'S'))
            ).to_dict()

            ejSSO[col] = pd.Series(
                self.getSSO(['E', 'J'], df[col].astype(int).apply(
                    lambda ele: 'J' if ele % 2 else 'E'))
            ).to_dict()

            ejSNO[col] = pd.Series(
                self.getSNO(['E', 'J'], df[col].astype(int).apply(
                    lambda ele: 'J' if ele % 2 else 'E'))
            ).to_dict()

        result['dsSSO'] = dsSSO
        result['dsSNO'] = dsSNO
        result['ejSSO'] = ejSSO
        result['ejSNO'] = ejSNO

        return result

class GameLotteryViewSetSSC(LotteryAnaBase):
    """
    1. ** ballCount: ** &#8194 單一號碼 累積開出次數
    2. ** ballSNO: ** &#8194 單一號碼 連續「未開出」次數
    3. ** ballSSO: ** &#8194 單一號碼 連續「開出」次數
    4. ** ballDSCount: ** &#8194 單碼 大小 累積開出次數
    5. ** ballEJCount: ** &#8194 單碼 單雙 累積開出次數
    6. ** ballHEJCount: ** &#8194 單碼 合單雙 累積開出次數
    7. ** ballTDSCount: ** &#8194 單碼 尾大小 累積開出次數
    8. ** ballAnimalCount: ** &#8194 單碼 生肖 累積開出次數
    9. ** ballColorCount: ** &#8194 單碼 色波 累積開出次數
    10. ** ballColorDSCount: ** &#8194 單碼 色波x大小 混和盤 累積開出次數
    11. ** ballColorEJCount: ** &#8194 單碼 色波x單雙 混和盤 累積開出次數
    12. ** ballColorDSEJCount: ** &#8194 單碼 色波x大小x單雙 混和盤 累積開出次數
    13. ** DSCombCount: ** &#8194 大小組合 累積開出次數
    14. ** EJCombCount: ** &#8194 單雙組合 累積開出次數
    15. ** tailCount: ** &#8194 尾數 累積開出次數
    16. ** totalDSCount: ** &#8194 五碼(六碼)總和大小 累積開出次數
    17. ** totalEJCount: ** &#8194 五碼(六碼)總和單雙 累積開出次數
    18. ** THCount: ** &#8194 台號 累積開出次數
    19. ** TSCount: ** &#8194 特三 累積開出次數
    """

    def data_manipulate(self, df):
        super().data_manipulate(df)

        result = {}

        ##### 單碼相關分析 #####
        if Playkey in ["WSJLHC", "WNWSJLHC", "CAF5WSJLHC"]:
            position = ['A1', 'A2', 'A3', 'A4', 'A5']
            df[position] = df['number'].str.split(',', n=5, expand=True)
            balls = [str(ele).zfill(2) for ele in range(1, 40)]
            blue = ["02", "05", "08", "11", "14", "17",
                    "20", "23", "26", "29", "32", "35", "38"]
            red = ["01", "04", "07", "10", "13", "16",
                   "19", "22", "25", "28", "31", "34", "37"]
            dsCriteria = 19
            sdsCriteria = 19
        elif Playkey == "WLCLHC":
            position = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'Special']
            df['number'] = df['number'].str.replace('+', ',')
            df[position] = df['number'].str.split(',', n=7, expand=True)
            balls = [str(ele).zfill(2) for ele in range(1, 38)]
            blue = ["02", "05", "08", "11", "14", "17",
                    "20", "23", "26", "29", "32", "35", "38"]
            red = ["01", "04", "07", "10", "13", "16",
                   "19", "22", "25", "28", "31", "34", "37"]
            dsCriteria = 19
            sdsCriteria = 4
        else:
            position = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'Special']
            df['number'] = df['number'].str.replace('+', ',')
            df[position] = df['number'].str.split(',', n=7, expand=True)
            balls = [str(ele).zfill(2) for ele in range(1, 50)]
            blue = ["03", "04", "09", "10", "14", "15", "20", "25",
                    "26", "31", "36", "37", "41", "42", "47", "48"]
            red = ["01", "02", "07", "08", "12", "13", "18", "19",
                   "23", "24", "29", "30", "34", "35", "40", "45", "46"]
            dsCriteria = 24
            sdsCriteria = 24

        numCand = pd.DataFrame({'ball': balls})
        numCand['DS'] = numCand['ball'].astype(int).apply(
            lambda ele: 'D' if ele > dsCriteria else 'S')
        numCand['EJ'] = numCand['ball'].astype(int).apply(
            lambda ele: 'J' if ele % 2 else 'E')
        numCand['color'] = numCand['ball'].apply(
            lambda ele: 'B' if ele in blue else 'R' if ele in red else 'G')
        numCand['Tail'] = numCand['ball'].astype(
            int).apply(lambda ele: ele % 10)
        numCand['TDS'] = numCand['Tail'].apply(
            lambda ele: 'TD' if ele > 4 else 'TS')
        numCand['HEJ'] = numCand['ball'].astype(int).apply(
            lambda ele: "HJ" if (ele // 10 + ele % 10) % 2 else "HE")
        numCand['HDS'] = numCand['ball'].astype(int).apply(
            lambda ele: 'HD' if (ele // 10 + ele % 10) > 6 else 'HS')
        numCand['Ann'] = numCand['ball'].astype(
            int).apply(lambda ele: (ele-1) % 12 + 1)
        numCand['ColorEJ'] = numCand['color'] + "_" + numCand['EJ']
        numCand['ColorDS'] = numCand['color'] + "_" + numCand['DS']
        numCand['ColorDSEJ'] = numCand['color'] + \
            "_" + numCand['DS'] + numCand['EJ']

        isWLC = (Playkey == "WLCLHC")

        # 特碼專用 candiate
        if isWLC:
            specialCand = numCand.loc[numCand['ball'].isin(balls[:8])]
            specialCand['DS'] = numCand['ball'].astype(int).apply(
                lambda ele: 'D' if ele > sdsCriteria else "S"
            )
        
        # 用 ZMPositin 去代替position使用
        if isWLC:
            ZMPosition = position[:-1]
        else:
            ZMPosition = position


        # 單碼 各球累積開出次數
        ballCount = df[ZMPosition].apply(
            pd.value_counts).rename_axis(index='ball').reset_index()
        ballCount = pd.merge(numCand, ballCount, how='outer').fillna(
            0).set_index('ball')

        result['ballCount'] = ballCount[ZMPosition].sum(axis=1).to_dict()

        if isWLC:
            specialCount = df[['Special']] \
            .apply(pd.value_counts).rename_axis(index='ball').reset_index()

            specialCount = pd.merge(specialCand, specialCount, how='outer')\
                .fillna(0).set_index('ball')
            result['specialCount'] = specialCount['Special'].to_dict()

        # 單碼 大小累積開出次數
        ballDSCount = ballCount.groupby('DS')[ZMPosition].sum().to_dict()
        if isWLC:
            specialDSCount = specialCount.groupby(
            'DS')[['Special']].sum().to_dict()
            ballDSCount.update(specialDSCount)
        result['ballDSCount'] = ballDSCount

        # 單碼 單雙累積開出次數
        ballEJCount = ballCount.groupby('EJ')[ZMPosition].sum().to_dict()
        if isWLC:
            specialEJCount = specialCount \
                .groupby('EJ')[['Special']] \
                    .sum().to_dict()
            ballEJCount.update(specialEJCount)
        result['ballEJCount'] = ballEJCount

        # 單碼 色波累積開出次數
        ballColorCount = ballCount.groupby('color')[ZMPosition].sum().to_dict()
        result['ballColorCount'] = ballColorCount

        # 單碼 生肖累積開出次數
        ballAnimalCount = ballCount.groupby('Ann')[ZMPosition].sum().to_dict()
        result['ballAnimalCount'] = ballAnimalCount

        # 單碼 混和盤 (顏色 x 單雙)
        ballColorEJCount = ballCount \
            .groupby('ColorEJ')[ZMPosition].sum().to_dict()
        result['ballColorEJCount'] = ballColorEJCount

        # 單碼 混和盤 (顏色 x 大小)
        ballColorDSCount = ballCount.groupby(
            'ColorDS')[ZMPosition].sum().to_dict()
        result['ballColorDSCount'] = ballColorDSCount

        # 單碼 混和盤 (顏色 x 大小 x 單雙)
        ballColorDSEJCount = ballCount.groupby(
            'ColorDSEJ')[ZMPosition].sum().to_dict()
        result['ballColorDSEJCount'] = ballColorDSEJCount

        # 單碼 尾大小 累積開出次數
        ballTDSCount = ballCount.groupby('TDS')[ZMPosition].sum().to_dict()

        if isWLC:
            specialTDSCount = specialCount.groupby(
            'TDS')[['Special']].sum().to_dict()
            ballTDSCount.update(specialTDSCount)
        result['ballTDSCount'] = ballTDSCount

        # 單碼 合單雙 累積開出次數
        ballHEJCount = ballCount.groupby('HEJ')[ZMPosition].sum().to_dict()

        if isWLC:
            specialHEJCount = specialCount.groupby(
            'TDS')[['Special']].sum().to_dict()
            ballHEJCount.update(specialHEJCount)
        result['ballHEJCount'] = ballHEJCount

        ###### 每一個號碼 連續未開出次數 | 連續開出次數  #####
        if isWLC:
            df['ZM'] = df['number'].str.split(',').str[:-1]
        else:
            df['ZM'] = df['number'].str.split(',')
        ballSNO = pd.Series(self.getSNO(balls, df['ZM']))  # 連續未開出
        ballSSO = pd.Series(self.getSSO(balls, df['ZM']))  # 連續開出
        result['ballSNO'] = ballSNO.to_dict()
        result['ballSSO'] = ballSSO.to_dict()

        if isWLC:
            specialSNO = pd.Series(self.getSNO(balls[:8], df['Special']))
            specialSSO = pd.Series(self.getSSO(balls[:8], df['Special']))
            result['specialSNO'] = specialSNO.to_dict()
            result['specialSSO'] = specialSSO.to_dict()

        ##### 大小組合 #####
        DSCombCount = df[position].astype(int).apply(
            lambda ele: ele > dsCriteria).sum(axis=1).value_counts()
        DSCombCount.index = [
            'D' + str(ele) + 'S' + str(len(position) - ele) for ele in DSCombCount.index]

        ##### 單雙組合 #####
        EJCombCount = df[position].astype(int).apply(
            lambda ele: ele % 2).sum(axis=1).value_counts()
        EJCombCount.index = ['J'+str(ele)+"E"+str(len(position)-ele)
                             for ele in EJCombCount.index]

        result['EJCombCount'] = DSCombCount.to_dict()
        result['DSCombCount'] = EJCombCount.to_dict()

        ##### 尾數 累積開出次數  #####
        tailCount = ballCount.groupby('Tail')[ZMPosition].sum().sum(axis=1)
        tailCount.index = [('T'+str(ele)) for ele in tailCount.index]
        tailCount = tailCount.to_dict()
        if isWLC:
            specialTailCount = specialCount.groupby('Tail')[['Special']].sum()
            specialTailCount.index = [('T'+str(ele)) for ele in specialTailCount.index]
            specialTailCount = specialTailCount.to_dict()['Special']

            for tail, values in specialTailCount.items():
                if tail in tailCount:
                    tailCount[tail] += values
                else:
                    tailCount[tail] = values

        result['tailCount'] = tailCount

        ##### 台號 | 天三 累積開出次數  #####
        def getTH(ls):
            if Playkey in ["WSJLHC", "WNWSJLHC", "CAF5WSJLHC", "WLCLHC"]:
                temp = sorted(ls)
            else:
                temp = sorted(ls[:-1])

            listLength = len(temp)
            TH = []
            TS = ''.join([ele[-1] for ele in temp[2:5]])

            for i in range(0, listLength-1):
                TH.append(temp[i][-1]+temp[i+1][-1])

            return TH, TS

        df['TH'], df['TS'] = zip(*df['ZM'].apply(getTH))

        # 台號
        THCount = pd.DataFrame(df.TH.to_list()).stack().value_counts()
        result['THCount'] = THCount.to_dict()

        # 特三
        TSCount = df.groupby('TS').size()
        result['TSCount'] = TSCount.to_dict()

        ##### 總和 大小 | 單雙 #####
        totalCount = df[list(filter(lambda ele: ele != 'Special', position))] \
            .astype(int).sum(axis=1) \
            .value_counts() \
            .reset_index() \
            .rename(columns={'index': 'total', 0: 'count'})

        totalDSCriteria = 99 if Playkey in [
            'WSJLHC', 'WNWSJLHC', "CAF5WSJLHC"] else 149
        totalCount['DS'] = totalCount['total'].apply(
            lambda ele: "D" if ele >= totalDSCriteria else "S")
        totalCount['EJ'] = totalCount['total'].apply(
            lambda ele: "J" if ele % 2 else "E")

        totalDSCount = totalCount.groupby('DS')['count'].sum()
        totalEJCount = totalCount.groupby('EJ')['count'].sum()

        result['totalDSCount'] = totalDSCount.to_dict()
        result['totalEJCount'] = totalEJCount.to_dict()
                
        return result