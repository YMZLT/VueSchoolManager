from django.db import models
from rest_framework import fields, serializers
import Model.models as md


# 序列化

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.User
        fields = ['user_id', 'user_name', 'password', 'is_admin']

    def create(self, validated_data):
        instance = md.User.objects.create_superuser(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance

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
            user.set_password(user_data.get('password', user.password))
            user.save()
        if validated_data.get('college', instance.college):
            instance.college = md.CollegeTable(
                **validated_data.get('college', instance.college))
        if validated_data.get('English_class', instance.English_class):
            instance.English_class = validated_data.get(
                'English_class', instance.English_class)

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

    class Meta:
        model = md.CourseTable
        fields = ['course_id', 'course_name', 'credit']


class OpenSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.OpenTable
        fields = ['id','course', 'teacher', 'semaster', 'course_time']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.ScoreTable
        fields = ['student', 'open', 'score']
