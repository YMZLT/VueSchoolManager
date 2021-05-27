from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from Model.analysis import Analysis
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


class IsStudent(BasePermission):
    """
    学生用户拥有的权限
    """
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        user = request.user
        # print(user.user_id)
        if not user:
            return False
        if not user.user_type == 'S':
            return False
        return True


class StudentView(APIView):
    '''学生用户'''
    permission_classes = (IsAuthenticated, IsStudent,)


class StudentInfo(StudentView):
    """查看当前登录的学生用户信息
    """

    def get(self, request):
        user = request.user
        try:
            Student_instance = md.StudentTable.objects.get(pk=user.user_id)
        except md.StudentTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '该学生不存在！'
            }
            return Response(data)
        serializer = serializers.StudentSerializer(Student_instance)
        data = {
            'msg': 'success',
            'status': 200,
            'data': serializer.data
        }
        return Response(data)
        
    def put(self, request):
        """
        data: 传入原始密码，新密码
        """
        user = request.user  # 当前登录用户
        if check_password(request.data["password"], user.password):
            user.password = make_password(request.data["password_new"])
            user.save()
            data = {
                'msg': '密码修改成功',
                'status': 200,
                'detail': user.user_id
            }
            return Response(data)
        data = {
            'msg': '密码修改失败',
            'status': 400,
            'detail': '原始密码校验失败'
        }
        return Response(data)


@api_view(['GET'])
def Open_search(request):
    """按条件查询开课详细信息
    """
    query = request.query_params.dict()
    try:
        Open_instance = md.OpenTable.objects.filter(**query)
    except md.OpenTable.DoesNotExist:
        data = {
            'msg': '查询失败！',
            'status': 400,
            'detail': '数据不存在！'
        }
        return Response(data)
    serializer = serializers.OpenDetailSerializer(Open_instance, many=True)
    data = {
        'msg': '查询成功！',
        'status': 200,
        'total': len(serializer.data),
        'Opens': serializer.data,
    }
    return Response(data)

# 成绩/选课数据接口


class ScoreManager(StudentView):
    def post(self, request):
        """
        添加选课
        """
        query = request.query_params.dict()
        data = {
            "student": "",
            "open": ""
        }
        data["student"] = request.user.user_id
        data["open"] = query["open"]
        serializer = serializers.ScoreSerializer(
            data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'msg': '添加选课成功',
                'status': 200,
                'data': serializer.data,
            }
            return Response(data)
        data = {
            'msg': '添加选课失败',
            'status': 400,
            'detail': serializer.errors
        }
        return Response(data)

    def get(self, request):
        """按条件查询选课详细信息
        """
        query = request.query_params.dict()
        user = request.user
        try:
            Score_instance = md.ScoreTable.objects.filter(student=user.user_id)
            if "open" in query:
                Score_instance = Score_instance.filter(open=query["open"])
            if "teacher" in query:
                Score_instance = Score_instance.filter(
                    open__teacher=query["teacher"])
            if "semester" in query:
                Score_instance = Score_instance.filter(
                    open__semester=query["semester"])
            if "semester" in query:
                Score_instance = Score_instance.filter(
                    open__semester=query["semester"])
            if "course" in query:
                Score_instance = Score_instance.filter(
                    open__course=query["course"])
            if "course_time" in query:
                Score_instance = Score_instance.filter(
                    open__course_time=query["course_time"])
        except md.ScoreTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
        serializer = serializers.ScoreDetailSerializer_v2(
            Score_instance, many=True)
        data = {
            'msg': '查询成功',
            'status': 200,
            'Scores': serializer.data,
            'total': len(serializer.data),
        }
        return Response(data)

    def delete(self, request):
        """删除选课信息
        """
        query = request.query_params.dict()
        if not "open" in query:
            data = {
                'msg': '删除选课失败',
                'status': 400,
                'detail': '字段错误，缺少open字段！'
            }
            return Response(data)
        try:
            Score_instance = md.ScoreTable.objects.filter(open=query["open"])
        except md.ScoreTable.DoesNotExist:
            data = {
                'msg': '删除选课失败',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)

        Score_instance.delete()
        data = {
            'msg': '删除选课成功',
            'status': 200,
        }
        return Response(data)


class Score_Analysis(StudentView):
    """查询每学期的平均成绩
    """

    def get(self, request):
        Al = Analysis()
        user = request.user
        avgScore = Al.getAvgScore(user.user_id)
        data = {
            'data': avgScore,
            'msg': 'success',
            'status': 200
        }
        return Response(data)
