from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


@api_view(['GET'])
def Teacher_info(request):
    """按学号查询教师信息
    """
    query = request.query_params.dict()  # 变成字典
    try:
        Teacher_instance = md.TeacherTable.objects.get(pk=query['teacher_id'])
    except md.TeacherTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.TeacherSerializer(Teacher_instance)
    data = {
        'data': {
            'Teachers': serializer.data,
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)


@api_view(['GET'])
def Student_info(request):
    """按学号查询学生信息
    """
    query = request.query_params.dict()  # 变成字典
    try:
        Student_instance = md.StudentTable.objects.get(pk=query['student_id'])
    except md.StudentTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.StudentSerializer(Student_instance)
    data = {
        'data': {
            'Students': serializer.data,
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)


@api_view(['PUT'])
def Teacher_edit(request, format=None):
    """
    更新教师信息
    """
    query = request.query_params.dict()
    try:
        Teacher_instance = md.TeacherTable.objects.get(pk=query['teacher_id'])
    except md.TeacherTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.TeacherSerializer(
            Teacher_instance, data=request.data, partial=True)
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
            'status': 400,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET'])
def Score_search(request):
    """按条件查询选课信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        Score_instance = md.ScoreTable.objects.filter(**query)
    except md.ScoreTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.ScoreSerializer(Score_instance, many=True)
    data = {
        'data': {
            'Scores': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)


@api_view(['PUT'])
def Score_edit(request, format=None):
    """
    修改成绩信息
    """
    query = request.query_params.dict()  # 变成字典
    try:
        Score_instance = md.ScoreTable.objects.filter(**query).first()

    except md.ScoreTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.ScoreSerializer(
            Score_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Scores': serializer.data,
                },
                'msg': 'success',
                'status': 200
            }
            return Response(data)
        data = {
            'msg': 'error',
            'status': 400,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET'])
def Open_search(request):
    """按条件查询开课信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        Open_instance = md.OpenTable.objects.filter(**query)
    except md.OpenTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.OpenSerializer(Open_instance, many=True)
    data = {
        'data': {
            'Opens': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)
