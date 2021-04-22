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

    def create(self, user_id, user_name, user_type, password, is_admin,
               college_id=None, English_class=None, position=None):
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = User(
            user_id=user_id,
            user_name=user_name,
            user_type=user_type,
            is_admin=is_admin,
            college_id=CollegeTable(college_id['college_id']),
            English_class=English_class,
            position=position
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_id, user_name, user_type, password, is_admin,
                         college_id=None, English_class=None, position=None):
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = User(
            user_id=user_id,
            user_name=user_name,
            user_type='T',
            is_admin=True,
            college_id=CollegeTable(college_id['college_id']),
            position=position
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
    type_choices = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    user_type = models.CharField(max_length=2, choices=type_choices)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'user_id'
    #  用命令 createsuperuser 添加用户时,user_type,user_name 是需要提示用户填写的内容
    REQUIRED_FIELDS = ['user_type', 'user_name']

    # 可选字段
    college_id = models.ForeignKey(
        CollegeTable,on_delete=models.CASCADE, blank=True)  # 院系号
    English_class = models.CharField(
        max_length=2, blank=True)  # 英语等级（user_type=='S'时有效）
    position = models.CharField(
        max_length=10, blank=True)  # 职位（user_type=='T'时有效）

    def __str__(self):
        return self.user_id


class CourseTable(models.Model):  # 课程表(默认学分4，学时40)
    course_id = models.CharField(max_length=10, primary_key=True)  # 课号
    course_name = models.CharField(max_length=20)  # 课名
    credit = models.IntegerField(default=4)  # 学分
    credit_hour = models.IntegerField(default=40)  # 学时
    teacher_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 工号


class CourseOpenTable(models.Model):  # 开课表
    opencourse_id = models.IntegerField(primary_key=True)  # 开课标识号
    course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE)  # 课号
    semaster = models.CharField(max_length=20)  # 学期
    course_time = models.CharField(max_length=20)  # 上课时间


class ScoreTable(models.Model):  # 选课表
    student_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 学号
    opencourse_id = models.ForeignKey(
        CourseOpenTable, on_delete=models.CASCADE)  # 开课标识号
    score = models.FloatField(blank=True)  # 最终成绩
