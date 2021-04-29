from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers

from django.contrib.auth import authenticate


@api_view(['POST'])
def Login(request, format=None):
    """登录验证
    """
    user_data = request.data
    print('user_data', user_data)
    msg = ''
    status = 400
    user = authenticate(
        username=user_data['user_id'], password=user_data['password'])
    if user is not None:
        # A backend authenticated the credentials
        msg = 'login success'
        status = 200
    else:
        # No backend authenticated the credentials
        msg = 'login error'
        status = 400
    data = {
        'msg': msg,
        'status': status,
    }
    return Response(data)
