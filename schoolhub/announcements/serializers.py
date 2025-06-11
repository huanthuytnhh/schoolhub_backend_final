# announcements/serializers.py

from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__' # Bao gồm tất cả các trường từ model
        # Hoặc liệt kê rõ ràng các trường nếu bạn muốn kiểm soát chặt chẽ hơn:
        # fields = ['id', 'title', 'message', 'category', 'date', 'time', 'recipients', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] # Các trường này tự động được quản lý bởi Django