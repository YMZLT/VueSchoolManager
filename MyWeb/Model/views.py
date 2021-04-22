from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


# 院系数据接口
@api_view(['GET', 'POST'])
def College_list(request, format=None):
    """
    列出所有的Colleges，或者创建一个新的College。
    """
    if request.method == 'GET':
        Colleges = md.CollegeTable.objects.all()
        serializer = serializers.CollegeSerializer(Colleges, many=True)
        data = {
            'data': {
                'colleges': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
        serializer = serializers.CollegeSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'colleges': serializer.data,
                },
                'msg': 'success',
                'status': 200
            }
            return Response(data)
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def College_detail(request, college_id, format=None):
    """
    获取，更新或删除一个College实例。
    """
    try:
        College_instance = md.CollegeTable.objects.get(pk=college_id)
    except md.CollegeTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.CollegeSerializer(College_instance)
        data = {
            'data': {
                'colleges': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.CollegeSerializer(
            College_instance, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'colleges': serializer.data,
                },
                'msg': 'success',
                'status': 200
            }
            return Response(data)
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)

    elif request.method == 'DELETE':
        College_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)
