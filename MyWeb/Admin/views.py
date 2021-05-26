from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers

@api_view(['POST'])
def SuperUser_create(request, format=None):
    """
    创建SuperUser
    """
    if request.method == 'POST':
        serializer = serializers.SuperUserSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'SuperUser': serializer.data,
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


@api_view(['POST'])
def SuperUser_create(request, format=None):
    """
    创建SuperUser
    """
    if request.method == 'POST':
        serializer = serializers.SuperUserSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'SuperUser': serializer.data,
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


@api_view(['PUT', 'DELETE'])
def SuperUser_edit(request, user_id, format=None):
    """
    更新或删除一个SuperUser实例。
    """
    try:
        SuperUser_instance = md.User.objects.filter(
            is_admin=True).get(pk=user_id)
    except md.User.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.SuperUserSerializer(
            SuperUser_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'SuperUsers': serializer.data,
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

    elif request.method == 'DELETE':
        SuperUser_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


@api_view(['GET'])
def SuperUser_search(request):
    """按条件查询院系信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        SuperUser_instance = md.User.objects.filter(is_admin=True).filter(**query)
    except md.User.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.SuperUserSerializer(SuperUser_instance, many=True)
    data = {
        'data': {
            'SuperUsers': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)

# 院系数据接口


@api_view(['POST'])
def College_create(request, format=None):
    """
    创建College
    """
    if request.method == 'POST':
        serializer = serializers.CollegeSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Colleges': serializer.data,
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


@api_view(['PUT', 'DELETE'])
def College_edit(request, college_id, format=None):
    """
    更新或删除一个College实例。
    """
    try:
        College_instance = md.CollegeTable.objects.get(pk=college_id)
    except md.CollegeTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.CollegeSerializer(
            College_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Colleges': serializer.data,
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

    elif request.method == 'DELETE':
        College_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


@api_view(['GET'])
def College_search(request):
    """按条件查询院系信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        College_instance = md.CollegeTable.objects.filter(**query)
    except md.CollegeTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.CollegeSerializer(College_instance, many=True)
    data = {
        'data': {
            'Colleges': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)

# 学生数据接口


@api_view(['POST'])
def Student_create(request, format=None):
    """
    创建一个新的Student
    """
    if request.method == 'POST':
        serializer = serializers.StudentSerializer(
            data=request.data, many=True)
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


@api_view(['PUT', 'DELETE'])
def Student_edit(request, student_id, format=None):
    """
    更新或删除一个Student实例
    """
    try:
        Student_instance = md.StudentTable.objects.get(user=student_id)
        user_instance = md.User.objects.get(user_id=student_id)
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

    elif request.method == 'DELETE':
        Student_instance.delete()
        user_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


@api_view(['GET'])
def Student_search(request):
    """按条件查询学生信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        Student_instance = md.StudentTable.objects.filter(**query)
    except md.StudentTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.StudentSerializer(Student_instance, many=True)
    data = {
        'data': {
            'Students': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)

# 教师数据接口


@api_view(['POST'])
def Teacher_create(request, format=None):
    """
    创建一个新的Teacher
    """
    if request.method == 'POST':
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
            'status': 400,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['PUT', 'DELETE'])
def Teacher_edit(request, teacher_id, format=None):
    """
    更新或删除一个Teacher实例
    """
    try:
        Teacher_instance = md.TeacherTable.objects.get(user=teacher_id)
        user_instance = md.User.objects.get(user_id=teacher_id)
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

    elif request.method == 'DELETE':
        Teacher_instance.delete()
        user_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


@api_view(['GET'])
def Teacher_search(request):
    """按条件查询教师信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    try:
        Teacher_instance = md.TeacherTable.objects.filter(**query)
    except md.TeacherTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.TeacherSerializer(Teacher_instance, many=True)
    data = {
        'data': {
            'Teachers': serializer.data,
            'total': len(serializer.data)
        },
        'msg': 'success',
        'status': 200
    }
    return Response(data)

# 课程数据接口


@api_view(['POST'])
def Course_create(request, format=None):
    """
    创建新的Course
    """
    if request.method == 'POST':
        serializer = serializers.CourseSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Courses': serializer.data,
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


@api_view(['PUT', 'DELETE'])
def Course_edit(request, course_id, format=None):
    """
    更新或删除一个Course实例。
    """
    try:
        Course_instance = md.CourseTable.objects.get(pk=course_id)
    except md.CourseTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    if request.method == 'PUT':
        serializer = serializers.CourseSerializer(
            Course_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Courses': serializer.data,
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

    elif request.method == 'DELETE':
        Course_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
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

# 开课数据接口


@api_view(['POST'])
def Open_create(request, format=None):
    """
    创建新的开课数据。
    """

    if request.method == 'POST':
        serializer = serializers.OpenSerializer(
            data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Opens': serializer.data,
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


@api_view(['PUT', 'DELETE'])
def Open_edit(request, open_id, format=None):
    """
    更新或删除一个Open实例。
    """
    try:
        Open_instance = md.OpenTable.objects.get(pk=open_id)
    except md.OpenTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'PUT':
        serializer = serializers.OpenSerializer(
            Open_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': {
                    'Opens': serializer.data,
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

    elif request.method == 'DELETE':
        Open_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
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
@api_view(['GET'])
def Open_search_detail(request):
    """按条件查询开课详细信息

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
    serializer = serializers.OpenDetailSerializer(Open_instance, many=True)
    data = {
        'data': {
            'Opens': serializer.data,
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
            data=request.data, many=True,partial=True)
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
    
@api_view(['GET'])
def Score_search_detail(request):
    """按条件查询选课详细信息

    Args:
        request: 请求

    Returns:
        data: 返回错误信息或正确的数据
    """
    # 根据学号和学期查询选课信息
    # request.query_params返回解析之后的查询字符串数据
    query = request.query_params.dict()  # 变成字典
    
     
    try:
        Score_instance = md.ScoreTable.objects.all()
        if "student" in query:
            Score_instance = Score_instance.filter(student=query["student"])
        if "open" in query:
            Score_instance = Score_instance.filter(open=query["open"])
        if "teacher" in query:
            Score_instance = Score_instance.filter(open__teacher=query["teacher"])
        if "semester" in query:
            Score_instance = Score_instance.filter(open__semester=query["semester"])
        if "semester" in query:
            Score_instance = Score_instance.filter(open__semester=query["semester"])
        if "course" in query:
            Score_instance = Score_instance.filter(open__course=query["course"])
        if "course_time" in query:
            Score_instance = Score_instance.filter(open__course_time=query["course_time"])
    except md.ScoreTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.ScoreDetailSerializer(Score_instance, many=True)
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

from .analysis import Analysis
@api_view(['GET'])
def Score_Analysis(request,semester):
    """按学期查询成绩的参数分布
    Args:
        request: 请求
        semester：学期
    Returns:
        data: 返回错误信息或正确的数据
    """
    Al = Analysis()
    basicData = Al.getBasicData(semester)
    distribution = Al.getScoreDistribution(semester)
    data = {
        'basicData': basicData,
        'distribution':distribution,
        'msg': 'success',
        'status': 200
    }
    return Response(data)

