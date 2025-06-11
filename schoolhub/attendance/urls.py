# attendance/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet

router = DefaultRouter()
# Đăng ký ViewSet với base name là 'attendance'
# URL sẽ là /api/attendances/ (nếu prefix trong project urls là 'api/')
router.register(r'attendances', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]