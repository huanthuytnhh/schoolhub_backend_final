from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # Include all fields from the Student model
        # Alternatively, you can specify fields explicitly:
        # fields = [
        #     'id', 'name', 'grade', 'rollNumber', 'isPresent', 'avatar',
        #     'gender', 'email', 'phoneNumber', 'dateOfBirth', 'password'
        # ]
