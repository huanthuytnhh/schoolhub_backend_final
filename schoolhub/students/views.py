from django.shortcuts import render

# students/views.py

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# View for listing all students and creating new students
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all() # The set of objects that the view will operate on
    serializer_class = StudentSerializer # The serializer to use for validation and serialization

# View for retrieving, updating, and deleting a single student
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all() # The set of objects that the view will operate on
    serializer_class = StudentSerializer # The serializer to use for validation and serialization
    lookup_field = 'pk' # The URL keyword argument that should be used to lookup the object. Default is 'pk' (primary key).
