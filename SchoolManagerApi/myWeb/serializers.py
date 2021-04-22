from rest_framework import serializers
from .models import CollegeTable, CourseTable, CourseOpenTable, ScoreTable
from .models import User


# 序列化
class UserSerializer(serializers.ModelSerializer):
    college_id = serializers.CharField(source='college_id.college_id')

    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_type', 'password',
                  'is_admin', 'college_id', 'English_class', 'position']


class TeacherSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=10)
    user_name = serializers.CharField(max_length=20)
    password = serializers.CharField()
    college_id = serializers.CharField(source='college_id.college_id')
    position = serializers.CharField(max_length=10)
    is_admin = serializers.BooleanField()

    def create(self, validated_data):
        return User.objects.create(user_id=validated_data["user_id"],
                                   user_name=validated_data["user_name"],
                                   user_type='T',
                                   password=validated_data["password"],
                                   is_admin=validated_data["is_admin"],
                                   college_id=validated_data["college_id"],
                                   English_class="",
                                   position=validated_data["position"])

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get(
            'user_name', instance.user_name)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.college_id = CollegeTable(validated_data.get(
            'college_id', instance.college_id))
        instance.position = validated_data.get(
            'position', instance.position)
        instance.save()
        return instance


class StudentSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=10)
    user_name = serializers.CharField(max_length=20)
    password = serializers.CharField()
    college_id = serializers.CharField(source='college_id.college_id')
    English_class = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return User.objects.create(user_id=validated_data["user_id"],
                                   user_name=validated_data["user_name"],
                                   user_type='S',
                                   password=validated_data["password"],
                                   is_admin=False,
                                   college_id=validated_data["college_id"],
                                   English_class=validated_data["English_class"], position="")

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get(
            'user_name', instance.user_name)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.college_id = CollegeTable(validated_data.get(
            'college_id', instance.college_id))
        instance.English_class = validated_data.get(
            'English_class', instance.English_class)
        instance.save()
        return instance


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeTable
        fields = ['college_id', 'college_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTable
        fields = ['course_id', 'course_name',
                  'credit', 'credit_hour', 'teacher_id']


class CourseOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOpenTable
        fields = ['opencourse_id', 'course_id', 'semaster', 'course_time']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreTable
        fields = ['student_id', 'opencourse_id', 'score']
