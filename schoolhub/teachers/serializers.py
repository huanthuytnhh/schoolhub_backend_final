# teachers/serializers.py

from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        # fields = ['id', 'name', 'email', 'phone', 'gender', 'avatar', 'classInCharge', 'dateOfBirth', 'password']
