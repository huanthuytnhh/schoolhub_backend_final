# teachers/urls.py

from django.urls import path
from .views import TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView, get_user_role

urlpatterns = [
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-detail'),
    path('user-role/', get_user_role, name='get-user-role'),
]
