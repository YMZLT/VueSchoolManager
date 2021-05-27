# from Student.views import StudentView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers

class IsTeacher(BasePermission):
    """
    教师用户拥有的权限
    """
    message = 'You do not have teacher permission to perform this action.'

    def has_permission(self, request, view):
        user = request.user
        print(user.user_id)
        if not user:
            return False
        if not user.user_type == 'T':
            return False
        return True

class TeacherView(APIView):
    '''教师用户'''
    permission_classes = (IsAuthenticated, IsTeacher,)
    
class Teacher_info(TeacherView):
    """查询教师信息
    """
    def get(self,request):
        user = request.user
        try:
            Teacher_instance = md.TeacherTable.objects.get(pk=user.user_id)
        except md.TeacherTable.DoesNotExist:
            data = {
                'msg': '查询失败',
                'status': 400,
                'detail': '该教师不存在！'
            }
            return Response(data)
        serializer = serializers.TeacherSerializer(Teacher_instance)
        data = {
            'msg': '查询成功',
            'status': 200,
            'data': serializer.data,
        }
        return Response(data)

class Student_info(TeacherView):
    """按学号查询学生信息
    """
    def get(self,request):
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

class Teacher_edit(TeacherView):
    """
    更新当前登录的教师信息
    """
    def put(self,request):
        user = request.user
        try:
            Teacher_instance = md.TeacherTable.objects.get(pk=user.user_id)
        except md.TeacherTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)

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

class Score_search(TeacherView):
    """按条件查询选课详细信息
    """
    def get(self,request):
        query = request.query_params.dict()  # 变成字典
        try:
            if "teacher" in query:
                Score_instance = md.ScoreTable.objects.filter(open__teacher=query["teacher"])
            if "student" in query:
                Score_instance = Score_instance.filter(student=query["student"])
            if "open" in query:
                Score_instance = Score_instance.filter(open=query["open"])
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

class Score_edit(TeacherView):
    """
    修改成绩信息
    """
    def put(self,request):
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

class Open_search(TeacherView):
    """按条件查询开课详细信息
    """
    def get(self,request):
        user = request.user
        query = request.query_params.dict()  # 变成字典
        try:
            Open_instance = md.OpenTable.objects.filter(teacher=user.user_id)
            Open_instance = Open_instance.filter(**query)
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

#上传教学大纲接口
from rest_framework.viewsets import GenericViewSet
# class BookInfoViewSet(GenericViewSet):
	# 保存图片
@api_view(['POST'])
def Save_pdf(request):
    file = request.FILES.get('file')
    try:
        # 构造文件保存路径
        file_path = './teachingschedule/files/' + file.name
        # 保存文件
        with open(file_path, 'wb+') as f:
            f.write(file.read())
            f.close()
        response = {'file': file.name, 'code': 200, 'msg': "添加成功"}
    except:
        response = {'file': '', 'code': 201, 'msg': "添加失败"}
    return Response(response)



