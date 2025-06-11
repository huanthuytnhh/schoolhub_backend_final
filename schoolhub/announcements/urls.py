# announcements/urls.py

from django.urls import path
from .views import (
    AnnouncementListCreateAPIView,
    AnnouncementRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('announcements/', AnnouncementListCreateAPIView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementRetrieveUpdateDestroyAPIView.as_view(), name='announcement-detail'),
]