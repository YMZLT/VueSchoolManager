from django.db import models
from rest_framework import fields, serializers
import Model.models as md


# 序列化
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.CollegeTable
        fields = ['college_id', 'college_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.User
        fields = ['user_id', 'user_name', 'password']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    college = serializers.CharField(source="college.college_id")

    class Meta:
        model = md.StudentTable
        fields = ['user', 'English_class', 'college']

    def create(self, validated_data):
        # 先将college字段pop出来备用
        user_data = validated_data.pop("user")
        user = md.User.objects.create(**user_data)

        # 然后再存储college,English_class
        instance = md.StudentTable.objects.create(user=user, **validated_data)
        return instance

    def update(self, instance, validated_data):

        if validated_data.get('user'):
            user_data = validated_data.pop("user")
            user = instance.user
            user.user_name = user_data.get('user_name', user.user_name)
            user.set_password(user_data.get('user_name', user.user_name))
            user.save()

        instance.English_class = validated_data.get(
            'English_class', instance.English_class)
        instance.college = md.CollegeTable(
            **validated_data.get('college', instance.college))
        instance.save()

        return instance


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    college = serializers.CharField(source="college.college_id")

    class Meta:
        model = md.TeacherTable
        fields = ['user', 'position', 'college']

    def create(self, validated_data):
        # 先将college字段pop出来备用
        user_data = validated_data.pop("user")
        user = md.User.objects.create(**user_data)

        # 然后再存储college,position
        instance = md.TeacherTable.objects.create(user=user, **validated_data)
        return instance

    def update(self, instance, validated_data):

        if validated_data.get('user'):
            user_data = validated_data.pop("user")
            user = instance.user
            user.user_name = user_data.get('user_name', user.user_name)
            user.set_password(user_data.get('user_name', user.user_name))
            user.save()

        instance.position = validated_data.get('position', instance.position)
        instance.college = md.CollegeTable(
            **validated_data.get('college', instance.college))
        instance.save()

        return instance


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.user')

    class Meta:
        model = md.CourseTable
        fields = ['course_id', 'course_name', 'credit', 'teacher']


class OpenSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.course_id')

    class Meta:
        model = md.OpenTable
        fields = ['open_id', 'course', 'semaster', 'course_time']


class ScoreSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user')
    open = serializers.CharField(source='open.open_id')

    class Meta:
        model = md.ScoreTable
        fields = ['student', 'open', 'score']
