from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer
# 1. 加载model
from myWeb import models

# 2. 加载Serializer
from myWeb import serializers


@api_view(['GET', 'POST'])
def User_list(request, format=None):
    """
    列出所有的Users，或者创建一个新的User。
    """
    if request.method == 'GET':
        User_instance = models.User.objects.all()
        serializer = serializers.UserSerializer(User_instance, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def User_detail(request, user_id, format=None):
    """
    获取，更新或删除一个User实例。
    """
    try:
        User_instance = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.UserSerializer(User_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.UserSerializer(
            User_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 学生数据接口


@api_view(['GET', 'POST'])
def Student_list(request, format=None):
    """
    列出所有的Students，或者创建一个新的Student。
    """
    if request.method == 'GET':
        Student_instance = models.User.objects.filter(user_type='S')
        serializer = serializers.StudentSerializer(Student_instance, many=True)
        data = {
            'data': {
                'students': serializer.data,
                'total': len(serializer.data)
            },
            'meta': {
                'msg': '数据不存在',
                'status': status.HTTP_404_NOT_FOUND
            }}
        json = JSONRenderer().render(data)
        return Response(json)

    elif request.method == 'POST':
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Student_detail(request, user_id, format=None):
    """
    获取，更新或删除一个Student实例。
    """
    try:
        Student_instance = models.User.objects.get(pk=user_id, user_type='S')
    except models.User.DoesNotExist:
        data = {'meta': {
            'msg': '数据不存在',
            'status': status.HTTP_404_NOT_FOUND
        }}
        json = JSONRenderer().render(data)
        return Response(json)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(Student_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.StudentSerializer(
            Student_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Student_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 教师数据接口
@api_view(['GET', 'POST'])
def Teacher_list(request, format=None):
    """
    列出所有的Teachers，或者创建一个新的Teacher。
    """
    if request.method == 'GET':
        Teacher_instance = models.User.objects.filter(user_type='T')
        serializer = serializers.TeacherSerializer(Teacher_instance, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Teacher_detail(request, user_id, format=None):
    """
    获取，更新或删除一个Teacher实例。
    """
    try:
        Teacher_instance = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.TeacherSerializer(Teacher_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.TeacherSerializer(
            Teacher_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Teacher_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# 院系数据接口


@api_view(['GET', 'POST'])
def College_list(request, format=None):
    """
    列出所有的Colleges，或者创建一个新的College。
    """
    if request.method == 'GET':
        Colleges = models.CollegeTable.objects.all()
        serializer = serializers.CollegeSerializer(Colleges, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def College_detail(request, College_id, format=None):
    """
    获取，更新或删除一个College实例。
    """
    try:
        College_instance = models.CollegeTable.objects.get(pk=College_id)
    except models.CollegeTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CollegeSerializer(College_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.CollegeSerializer(
            College_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        College_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 课程数据接口
@api_view(['GET', 'POST'])
def Course_list(request, format=None):
    """
    列出所有的Courses，或者创建一个新的Course。
    """
    if request.method == 'GET':
        Courses = models.CourseTable.objects.all()
        serializer = serializers.CourseSerializer(Courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Course_detail(request, Course_id, format=None):
    """
    获取，更新或删除一个Course实例。
    """
    try:
        Course_instance = models.CourseTable.objects.get(pk=Course_id)
    except models.CourseTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CourseSerializer(Course_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.CourseSerializer(
            Course_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Course_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 开课数据接口
@api_view(['GET', 'POST'])
def CourseOpen_list(request, format=None):
    """
    列出所有的CourseOpens，或者创建一个新的CourseOpen。
    """
    if request.method == 'GET':
        CourseOpens = models.CourseOpenTable.objects.all()
        serializer = serializers.CourseOpenSerializer(CourseOpens, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.CourseOpenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def CourseOpen_detail(request, CourseOpen_id, format=None):
    """
    获取，更新或删除一个CourseOpen实例。
    """
    try:
        CourseOpen_instance = models.CourseOpenTable.objects.get(
            pk=CourseOpen_id)
    except models.CourseOpenTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CourseOpenSerializer(CourseOpen_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.CourseOpenSerializer(
            CourseOpen_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        CourseOpen_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 成绩数据接口
@api_view(['GET', 'POST'])
def Score_list(request, format=None):
    """
    列出所有的Scores，或者创建一个新的Score。
    """
    if request.method == 'GET':
        Scores = models.ScoreTable.objects.all()
        serializer = serializers.ScoreSerializer(Scores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Score_detail(request, student_id, format=None):
    """
    获取，更新或删除一个Score实例。
    """
    try:
        Score_instance = models.ScoreTable.objects.get(student_id=student_id)
    except models.ScoreTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ScoreSerializer(Score_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ScoreSerializer(
            Score_instance, data=request.data)
        print("serializer:", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("serializer.is_valid()", serializer.is_valid())

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Score_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
