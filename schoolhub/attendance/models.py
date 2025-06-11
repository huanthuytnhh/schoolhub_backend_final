# attendance/models.py
from django.db import models
from students.models import Student # Giả sử model Student của bạn ở app 'students'

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances_records') # Đổi related_name nếu 'attendances' đã được dùng
    # class_id lưu trữ định danh lớp, thường là student.grade tại thời điểm điểm danh
    class_id = models.CharField(max_length=50, db_index=True, help_text="Grade/Class identifier, e.g., '5/1'")
    date = models.DateField(db_index=True)
    is_present = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'date') # Mỗi học sinh chỉ có 1 bản ghi/ngày
        ordering = ['-date', 'student__name']

    def __str__(self):
        status = "Present" if self.is_present else "Absent"
        return f"{self.student.name} - {self.date.strftime('%Y-%m-%d')} - {status}"

    # Property để dễ dàng lấy student_id khi serialize, khớp với frontend mong đợi
    @property
    def student_id_prop(self): # Đặt tên khác để tránh trùng với field `student_id` nếu serializer tự tạo
        return self.student.id