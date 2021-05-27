from Model.analysis import Analysis
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
# 1. 加载model
from Model import models as md

# 2. 加载Serializer
from Model import serializers


class IsAdmin(BasePermission):
    """
    管理员用户拥有的权限
    """
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        user = request.user
        print(user.user_id)
        if not user:
            return False
        if not user.user_type == 'A':
            return False
        return True

class AdminView(APIView):
    '''管理员用户'''
    permission_classes = (IsAuthenticated, IsAdmin,)

class SuperUser_create(AdminView):
    def post(self, request):
        """
        创建SuperUser
        """
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

class SuperUser_create(AdminView):
    def post(self,request):
        """
        创建SuperUser
        """
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

class SuperUser_edit(AdminView):
    def put(self,request,user_id):
        """
        更新用户信息
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
    def delete(self,request,user_id):
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
        SuperUser_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)

class SuperUser_search(AdminView):
    
    def get(self,request):
        """按条件查询院系信息
        """
        query = request.query_params.dict()  # 变成字典
        try:
            SuperUser_instance = md.User.objects.filter(
                is_admin=True).filter(**query)
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

class College_create(AdminView):
    """
    创建College
    """
    def post(self,request):
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

class College_edit(AdminView):
    """
    更新或删除一个College实例。
    """
    def put(self,request, college_id):
        try:
            College_instance = md.CollegeTable.objects.get(pk=college_id)
        except md.CollegeTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
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
    def delete(self,request, college_id):
        try:
            College_instance = md.CollegeTable.objects.get(pk=college_id)
        except md.CollegeTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
        serializer = serializers.CollegeSerializer(
            College_instance, data=request.data, partial=True)

        College_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)

class College_search(AdminView):
    """按条件查询院系信息
    """
    def get(self,request):
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

class Student_create(AdminView):
    """
    创建一个新的Student
    """
    def post(self,request):
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

class Student_edit(AdminView):
    """
    更新或删除一个Student实例
    """
    def put(self,request, student_id):
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

    def delete(self,request, student_id):
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
        Student_instance.delete()
        user_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


class Student_search(AdminView):
    """按条件查询学生信息
    """
    def get(self,request):
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

class Teacher_create(AdminView):
    """
    创建一个新的Teacher
    """
    def post(self,request):
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

class Teacher_edit(AdminView):
    """
    更新或删除一个Teacher实例
    """
    def put(self,request, teacher_id):
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
    def delete(self,request, teacher_id):
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
        Teacher_instance.delete()
        user_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)

class Teacher_search(AdminView):
    """按条件查询教师信息
    """
    def get(self,request):
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


class Course_create(AdminView):

    """
    创建新的Course
    """
    def post(self,request):
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

class Course_edit(AdminView):
    """
    更新或删除一个Course实例。
    """
    def put(self,request, course_id):
        try:
            Course_instance = md.CourseTable.objects.get(pk=course_id)
        except md.CourseTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
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

    def delete(self,request,course_id):
        try:
            Course_instance = md.CourseTable.objects.get(pk=course_id)
        except md.CourseTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
        Course_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)


class Course_search(AdminView):
    """按条件查询课程信息
    """
    def get(self,request):
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


class Open_create(AdminView):
    """
    创建新的开课数据。
    """
    def post(self,request):
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

class Open_edit(AdminView):
    """
    更新或删除一个Open实例。
    """
    def put(self,request, open_id):
        try:
            Open_instance = md.OpenTable.objects.get(pk=open_id)
        except md.OpenTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
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

    def delete(self,request, open_id):
        try:
            Open_instance = md.OpenTable.objects.get(pk=open_id)
        except md.OpenTable.DoesNotExist:
            data = {
                'msg': 'error',
                'status': 400,
                'detail': '数据不存在！'
            }
            return Response(data)
        Open_instance.delete()
        data = {
            'msg': 'success',
            'status': 200,
        }
        return Response(data)

class Open_search(AdminView):
    """按条件查询开课信息
    """
    def get(self,request):
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

class Open_search_detail(AdminView):
    """按条件查询开课详细信息
    """
    def get(self,request):
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


class Score_create(AdminView):
    """
    创建一个新的Score。
    """
    def post(self,request):
        serializer = serializers.ScoreSerializer(
            data=request.data, many=True, partial=True)
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


class Score_search(AdminView):
    """按条件查询选课信息
    """
    def get(self,request):

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

class Score_search_detail(AdminView):
    """按条件查询选课详细信息
    """
    def get(self,request):

        query = request.query_params.dict()  # 变成字典

        try:
            Score_instance = md.ScoreTable.objects.all()
            if "student" in query:
                Score_instance = Score_instance.filter(student=query["student"])
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

class Score_delete(AdminView):
    """删除选课信息
    """
    def delete(self,request):
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

class Score_edit(AdminView):
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


class Score_Analysis(AdminView):
    """按学期查询成绩的参数分布
    Args:
        request: 请求
        semester：学期
    Returns:
        data: 返回错误信息或正确的数据
    """
    def get(self,request,semester):
        Al = Analysis()
        basicData = Al.getBasicData(semester)
        distribution = Al.getScoreDistribution(semester)
        data = {
            'basicData': basicData,
            'distribution': distribution,
            'msg': 'success',
            'status': 200
        }
        return Response(data)
