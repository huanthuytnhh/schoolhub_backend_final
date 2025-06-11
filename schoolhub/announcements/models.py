# announcements/models.py

from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=50) # Ví dụ: "Reminder", "Update", "Transaction"
    date = models.DateField() # Lưu trữ ngày (YYYY-MM-DD)
    time = models.TimeField() # Lưu trữ giờ (HH:MM:SS)
    recipients = models.JSONField(default=list) # Lưu trữ mảng chuỗi, mặc định là list rỗng

    # Optional: Thêm trường timestamp để theo dõi thời gian tạo/cập nhật
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date} {self.time})"

    class Meta:
        # Sắp xếp theo ngày giảm dần, sau đó theo thời gian giảm dần
        ordering = ['-date', '-time']
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"