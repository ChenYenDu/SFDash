from django.urls import path, re_path, include
from apps.GameInfo import views
from apps.GameInfo.analize import lottery, bet

# 開獎分析 API
urlpatterns = [
    path('lottery/pk/', lottery.GameLotteryViewSetPK.as_view()),
    path('lottery/ssc/', lottery.GameLotteryViewSetSSC.as_view()),
    path('lottery/lhc/', lottery.GameLotteryViewSetLHC.as_view()),
]

# BJL 模擬
urlpatterns += [
    path('stimulator/bjl_ver1/', views.bjlStimulator),
    path('stimulator/bjl_ver2/', views.bjlStimulatVer2),
    path('stimulator/bjlList/', views.BJLAdminListViewSet.as_view()),
    path('stimulator/bjlAdmin/<int:pk>/', views.BJLAdminDestroyViewSet.as_view()),
]

