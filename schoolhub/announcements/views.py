# announcements/views.py

from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer

class AnnouncementListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all announcements or creating a new announcement.
    GET /api/announcements/
    POST /api/announcements/
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single announcement.
    GET /api/announcements/{id}/
    PUT /api/announcements/{id}/
    PATCH /api/announcements/{id}/
    DELETE /api/announcements/{id}/
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk' # Sử dụng 'pk' (primary key) để tìm kiếm đối tượng