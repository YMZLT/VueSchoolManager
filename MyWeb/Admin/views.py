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

# 学生数据接口
@api_view(['GET', 'POST'])
def Student_list(request, format=None):
    """
    列出所有的Students，或者创建一个新的Student。
    """
    if request.method == 'GET':
        Students = md.StudentTable.objects.all()
        serializer = serializers.StudentSerializer(Students, many=True)
        data = {
            'data': {
                'Students': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def Student_detail(request, Student_id, format=None):
    """
    获取，更新或删除一个Student实例。
    """
    try:
        Student_instance = md.StudentTable.objects.get(user=Student_id)
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
def Teacher_detail(request, teacher_id, format=None):
    """
    获取，更新或删除一个Teacher实例。
    """
    try:
        Teacher_instance = md.TeacherTable.objects.get(user=teacher_id)
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


# 课程数据接口
@api_view(['GET', 'POST'])
def Course_list(request, format=None):
    """
    列出所有的Courses，或者创建一个新的Course。
    """
    if request.method == 'GET':
        Courses = md.CourseTable.objects.all()
        serializer = serializers.CourseSerializer(Courses, many=True)
        data = {
            'data': {
                'Courses': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def Course_detail(request, course_id, format=None):
    """
    获取，更新或删除一个Course实例。
    """
    try:
        Course_instance = md.CourseTable.objects.get(pk=course_id)
    except md.CourseTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.CourseSerializer(Course_instance)
        data = {
            'data': {
                'Courses': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.CourseSerializer(
            Course_instance, data=request.data,partial=True)

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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)

    elif request.method == 'DELETE':
        Course_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)


# 开课数据接口
@api_view(['GET', 'POST'])
def Open_list(request, format=None):
    """
    列出所有的Opens，或者创建一个新的Open。
    """
    if request.method == 'GET':
        Opens = md.OpenTable.objects.all()
        serializer = serializers.OpenSerializer(Opens, many=True)
        data = {
            'data': {
                'Opens': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def Open_detail(request, open_id, format=None):
    """
    获取，更新或删除一个Open实例。
    """
    try:
        Open_instance = md.OpenTable.objects.get(pk=open_id)
    except md.OpenTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.OpenSerializer(Open_instance)
        data = {
            'data': {
                'Opens': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.OpenSerializer(
            Open_instance, data=request.data,partial=True)

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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)

    elif request.method == 'DELETE':
        Open_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)


# 成绩/选课数据接口
@api_view(['GET', 'POST'])
def Score_list(request, format=None):
    """
    列出所有的Scores，或者创建一个新的Score。
    """
    if request.method == 'GET':
        Scores = md.ScoreTable.objects.all()
        serializer = serializers.ScoreSerializer(Scores, many=True)
        data = {
            'data': {
                'Scores': serializer.data,
                'total': len(serializer.data)
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'POST':
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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def Score_detail(request, student_id, format=None):
    """
    获取，更新或删除一个Score实例。
    """
    try:
        Score_instance = md.ScoreTable.objects.filter(student=student_id)
    except md.ScoreTable.DoesNotExist:
        data = {
            'msg': 'error',
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': '数据不存在！'
        }
        return Response(data)

    if request.method == 'GET':
        serializer = serializers.ScoreSerializer(Score_instance)
        data = {
            'data': {
                'Scores': serializer.data,
            },
            'msg': 'success',
            'status': 200
        }
        return Response(data)

    elif request.method == 'PUT':
        serializer = serializers.ScoreSerializer(
            Score_instance, data=request.data,partial=True)

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
            'status': status.HTTP_400_BAD_REQUEST,
            'detail': serializer.errors
        }
        return Response(data)

    elif request.method == 'DELETE':
        Score_instance.delete()
        data = {
            'msg': 'success',
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(data)