import datetime
import numpy as np
import pandas as pd
import functools import reduce
import json
import ast

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import Http404, HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.GameInfo.pagination import StandardResultSetPagination
from apps.GameInfo.serializer import BJLGoodRecordSerializer
from apps.GameInfo.analize.stimulator import ReverseBJL, BJLVer2

# Create your views here.

rBJL = ReverseBJL()

@api_view(['GET'])
def bjlStimulator(request):
    # rBJL = ReverseBJL()
    cut = request.GET.get('cut', '20')
    maxLength = int(request.GET.get('mLen', '6'))
    singleJumpTimes = int(request.GET.get('sjt', '0'))
    singleJumpMax = int(request.GET.get('sjm', '4'))
    doubleJumpTimes = int(request.GET.get('djt', '0'))
    doubleJumpMax = int(request.GET.get('djm', '4'))

    result, rounds, cards, details = rBJL.randomBuild(
        maxLength=maxLength,
        singleJumpTimes=singleJumpTimes,
        singleJumpMax=singleJumpMax,
        doubleJumpTimes=doubleJumpTimes,
        doubleJumpMax=doubleJumpMax
    )

    result = rBJL.reverseCut(result + cards, int(cut))
    del cards

    response = {
        'result': result,
        'rounds': rounds,
    }

    return JsonResponse(response, safe=False)

class BJLAdminListViewSet(ListAPIView):
    queryset = BJLGoodRecord.objects.using('data_write').all()
    serializer_class = BJLGoodRecordSerializer
    pagination_class = StandardResultSetPagination

class BJLAdminDestroyViewSet(DestroyAPIView):
    queryset = BJLGoodRecord.objects.using('data_write')

@api_view(['GET', 'POST'])
def bjlStimulatVer2(request):

    if request.method == 'GET':
        BJL = BJLVer2()
        # n = int(request.GET.get('n', '10'))
        longLen = request.GET.get("longLen", None)
        maxSingleLen = request.GET.get("maxSingleLen", None)
        maxDoubleLen = request.GET.get("maxDoubleLen", None)
        okRate = float(request.GET.get('okRate', '0.5'))
        cutStart = request.GET.get('cutStart', '150')
        cutEnd = request.GET.get('cutEnd', '280')

        # 長龍限制
        if longLen:
            longLen = int(longLen)

        # 單跳限制
        if maxSingleLen:
            maxSingleLen = int(maxSingleLen)

        # 雙跳限制
        if maxDoubleLen:
            maxDoubleLen = int(maxDoubleLen)

        # 切牌開始位置
        if cutStart:
            cutStart = int(cutStart)

        # 切牌結束位置
        if cutEnd:
            cutEnd = int(cutEnd)

        multiRoad = BJL.getMultiSetsWithTO(
            longLen=longLen, maxSingle=maxSingleLen, maxDouble=maxDoubleLen, okRate=okRate, cutStart=cutStart, cutEnd=cutEnd)

        response = {
            'multiRoad': multiRoad,
        }

        return JsonResponse(response, safe=False)

    else:

        reqData = request.data
        reqData['content'] = json.dumps(reqData['content'])
        reqData['created_at'] = datetime.datetime.now()

        data = {}

        try:
            BGR = BJLGoodRecord(**reqData)
            BGR.save(using='data_write')
            # serializer.save(using="dataana")
            data['error_code'] = 0
        except:
            return Response({'error_code': 1, }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data)
