
# from django.db.models.fields import CharField
from rest_framework import serializers
import Model.models as md
import Model.serializers as ms


# 序列化
class StudentSerializer(serializers.ModelSerializer):
    user = ms.UserSerializer(required=False)
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
            user.user_name = user_data.get('user_name',user.user_name)
            user.set_password(user_data.get('user_name',user.user_name))
            user.save()

        instance.English_class = validated_data.get('English_class', instance.English_class)
        instance.college = md.CollegeTable(**validated_data.get('college', instance.college))
        instance.save()

        return instance


