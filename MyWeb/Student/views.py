from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


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
def Student_edit(request,format=None):
    """
    更新学生信息
    """
    query = request.query_params.dict()
    try:
        Student_instance = md.StudentTable.objects.get(pk=query['student_id'])
    except md.StudentTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.StudentSerializer(
            Student_instance, data=request.data, partial=True)
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
            'status': 400,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET'])
def Course_search(request):
    """按条件查询课程信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        Course_instance = md.CourseTable.objects.filter(**query)
    except md.CourseTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.CourseSerializer(Course_instance, many=True)
    data = {
        'data': {
            'Courses': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)


# 成绩/选课数据接口
@api_view(['POST'])
def Score_create(request, format=None):
    """
    创建一个新的Score。
    """

    if request.method == 'POST':
        serializer = serializers.ScoreSerializer(
            data=request.data, many=True)
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


@api_view(['DELETE'])
def Score_delete(request):
    """删除选课信息

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

    if request.method == 'DELETE':
        Score_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)
