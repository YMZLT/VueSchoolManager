from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from . import serializers


# 教师数据接口
@api_view(['GET', 'POST'])
def Teacher_list(request, format=None):
    """
    列出所有的Teachers，或者创建一个新的Teacher。
    """
    if request.method == 'GET':
        Teachers = md.TeacherTable.objects.all()
        serializer = serializers.TeacherSerializer(Teachers, many=True)
        data = {
            'data': {
                'Teachers': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
        serializer = serializers.TeacherSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Teachers': serializer.data,
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
def Teacher_detail(request, Teacher_id, format=None):
    """
    获取，更新或删除一个Teacher实例。
    """
    try:
        Teacher_instance = md.TeacherTable.objects.get(user=Teacher_id)
    except md.TeacherTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.TeacherSerializer(Teacher_instance)
        data = {
            'data': {
                'Teachers': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.TeacherSerializer(
            Teacher_instance, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Teachers': serializer.data,
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
        Teacher_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)
