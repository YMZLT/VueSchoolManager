from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.conf import settings
from django.utils.tree import Node

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
        )
        user.set_password(password)
        user.save()
        return user


class CollegeTable(models.Model):  # 院系表
    college_id = models.CharField(max_length=10, primary_key=True)  # 院系号
    college_name = models.CharField(max_length=20)  # 名称

# 扩展用户模型


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=10, primary_key=True)  # 学号/工号
    user_name = models.CharField(max_length=20)  # 姓名
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # 模型管理
    objects = UserManager()
    USERNAME_FIELD = 'user_id'
    #  用命令 createsuperuser 添加用户时,user_type,user_name 是需要提示用户填写的内容
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_id


class StudentTable(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    English_class = models.CharField(
        max_length=2)  # 英语等级
    college = models.ForeignKey(
        CollegeTable, on_delete=models.CASCADE)  # 院系号


class TeacherTable(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=10)  # 职位
    college = models.ForeignKey(
        CollegeTable, on_delete=models.CASCADE)  # 院系号


class CourseTable(models.Model):  # 课程表(默认学分4，学时40)
    course_id = models.CharField(max_length=10, primary_key=True)  # 课号
    course_name = models.CharField(max_length=20)  # 课名
    credit = models.IntegerField(default=4)  # 学分
    teacher = models.ForeignKey(
        TeacherTable, on_delete=models.CASCADE)  # 工号


class OpenTable(models.Model):  # 开课表
    open_id = models.IntegerField(primary_key=True)  # 开课标识号
    course = models.ForeignKey(CourseTable, on_delete=models.CASCADE)  # 课号
    semaster = models.CharField(max_length=20)  # 学期
    course_time = models.CharField(max_length=20)  # 上课时间


class ScoreTable(models.Model):  # 选课表
    student = models.ForeignKey(
        StudentTable, on_delete=models.CASCADE)  # 学号
    open = models.ForeignKey(
        OpenTable, on_delete=models.CASCADE)  # 开课标识号
    score = models.FloatField(blank=True)  # 最终成绩
