from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.conf import settings

# Create your models here.


# 数据库同步命令

# 1.python manage.py makemigrations
# 2.python manage.py migrate

# 自定义用户管理
class UserManager(BaseUserManager):

    def create(self, user_id, user_name, password=None, is_admin=False):
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = User(
            user_id=user_id,
            user_name=user_name,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_id, user_name, password=None, is_admin=True):
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = User(
            user_id=user_id,
            user_name=user_name,
            is_admin=is_admin,
            user_type = 'A'
        )
        user.set_password(password)
        user.save()
        return user

class StudentManager(BaseUserManager):
    def create(self, user,English_class,college):
        if not user:
            raise ValueError('Users must have an user')
        user.user_type = 'S'
        student = StudentTable(
            user = user,
            English_class = English_class,
            college = CollegeTable(**college)
        )
        student.save()
        return student

class TeacherManager(BaseUserManager):
    def create(self, user,position,college):
        if not user:
            raise ValueError('Users must have an user')
        user.user_type = 'T'
        teacher = TeacherTable(
            user = user,
            position = position,
            college = CollegeTable(**college)
        )
        teacher.save()
        return teacher



class CollegeTable(models.Model):  # 院系表
    college_id = models.CharField(max_length=10, primary_key=True)  # 院系号
    college_name = models.CharField(max_length=20)  # 名称
    class Meta:
        db_table="CollegeTable"

# 扩展用户模型


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=10, primary_key=True)  # 学号/工号
    user_name = models.CharField(max_length=20)  # 姓名
    user_type = models.CharField(max_length=2,default='S') # 用户类型
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # 模型管理
    objects = UserManager()
    USERNAME_FIELD = 'user_id'
    #  用命令 createsuperuser 添加用户时,user_type,user_name 是需要提示用户填写的内容
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_id
    class Meta:
        db_table="User"


class StudentTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    English_class = models.CharField(
        max_length=2)  # 英语等级
    college = models.ForeignKey(
        CollegeTable, on_delete=models.CASCADE)  # 院系号
    objects = StudentManager()
    class Meta:
        db_table="StudentTable"


class TeacherTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    position = models.CharField(
        max_length=10)  # 职位
    college = models.ForeignKey(
        CollegeTable, on_delete=models.CASCADE)  # 院系号
    objects = TeacherManager()
    class Meta:
        db_table="TeacherTable"


class CourseTable(models.Model):  # 课程表(默认学分4，学时40)
    course_id = models.CharField(max_length=10, primary_key=True)  # 课号
    course_name = models.CharField(max_length=20)  # 课名
    credit = models.IntegerField(default=4)  # 学分
    class Meta:
        db_table="CourseTable"

    
class OpenTable(models.Model):  # 开课表
    course = models.ForeignKey(CourseTable, on_delete=models.CASCADE)  # 课号
    teacher = models.ForeignKey(
        TeacherTable, on_delete=models.CASCADE)  # 工号
    semester = models.CharField(max_length=20)  # 学期
    course_time = models.CharField(max_length=20)  # 上课时间
    class Meta:
        unique_together=("course","teacher","semester")
    class Meta:
        db_table="OpenTable"
    



class ScoreTable(models.Model):  # 选课表
    student = models.ForeignKey(
        StudentTable, on_delete=models.CASCADE)  # 学号
    open = models.ForeignKey(
        OpenTable, on_delete=models.CASCADE)  # 开课标识号
    score = models.FloatField(default=0)  # 最终成绩
    class Meta:
        unique_together=("student","open")
        db_table="ScoreTable"
