
# from django.db.models.fields import CharField
from rest_framework import serializers
import Model.models as md

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.User
        fields = ['user_id','user_name','password']
# 序列化
class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    college = serializers.CharField(source='college.college_id')
    class Meta:
        model = md.StudentTable
        fields = ['student', 'English_class','college']

    def create(self, validated_data):
        # 先将college字段pop出来备用
        student = validated_data.pop("student")
        user = md.User.objects.create(**student)
        
        # 然后再存储college,English_class
        instance = md.StudentTable(student=user,**validated_data)
        return instance