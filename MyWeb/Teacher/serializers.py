# from django.db.models.fields import CharField
from rest_framework import serializers
import Model.models as md
import Model.serializers as ms


# 序列化
class TeacherSerializer(serializers.ModelSerializer):
    user = ms.UserSerializer()
    college = serializers.CharField(source="college.college_id")
    class Meta:
        model = md.TeacherTable
        fields = ['user', 'position','college']

    def create(self, validated_data):
        # 先将college字段pop出来备用
        user_data = validated_data.pop("user")
        user = md.User.objects.create(**user_data)
        
        # 然后再存储college,position
        instance = md.TeacherTable.objects.create(user=user,**validated_data)
        return instance

    def update(self, instance, validated_data):

        if validated_data.get('user'):
            user_data = validated_data.pop("user")
            user = instance.user
            user.user_name = user_data.get('user_name',user.user_name)
            user.set_password(user_data.get('user_name',user.user_name))
            user.save()

        instance.position = validated_data.get('position', instance.position)
        instance.college = md.CollegeTable(**validated_data.get('college', instance.college))
        instance.save()

        return instance