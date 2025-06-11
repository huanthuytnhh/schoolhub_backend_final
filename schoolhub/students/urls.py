# students/urls.py

from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    # URL for listing all students and creating a new student
    # e.g., GET /api/students/, POST /api/students/
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),

    # URL for retrieving, updating, or deleting a specific student by ID
    # e.g., GET /api/students/1/, PUT /api/students/1/, DELETE /api/students/1/
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]
# This file defines the URL patterns for the student-related API endpoints.