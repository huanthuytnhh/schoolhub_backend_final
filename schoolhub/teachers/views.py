
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from .models import Teacher
from .serializers import TeacherSerializer
from students.serializers import StudentSerializer


@api_view(['GET'])
def get_user_role(request):
    email = request.GET.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)
    try:
        teacher = Teacher.objects.get(email=email)
        teacher_data = TeacherSerializer(teacher).data
        return Response({'role': teacher.role, 'user': teacher_data})
    except Teacher.DoesNotExist:
        try:
            student = Student.objects.get(email=email)
            student_data = StudentSerializer(student).data
            return Response({'role': 'student', 'user': student_data})
        except Student.DoesNotExist:
            return Response({'role': 'guest', 'user': None})
from django.shortcuts import render
# teachers/views.py

from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'pk'
