from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


# 学生信息数据
@api_view(['GET', 'PUT', 'DELETE'])
def Student_detail(request, student_id, format=None):
    """
    获取，更新或删除一个Student实例。
    """
    try:
        Student_instance = md.StudentTable.objects.get(user=student_id)
    except md.StudentTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(Student_instance)
        data = {
            'data': {
                'Students': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.StudentSerializer(
            Student_instance, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Students': serializer.data,
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
        Student_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)
