from django.db import models
from rest_framework import fields, serializers
import Model.models as md


# 序列化
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.CollegeTable
        fields = ['college_id', 'college_name']