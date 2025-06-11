# attendance/admin.py
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'class_id', 'date', 'is_present', 'notes')
    list_filter = ('date', 'class_id', 'is_present', 'student__grade') # Lọc theo grade của student
    search_fields = ('student__name', 'student__roll_number', 'notes', 'class_id')
    list_editable = ('is_present', 'notes') # Cho phép sửa nhanh từ danh sách

    def student_name(self, obj):
        return obj.student.name
    student_name.short_description = 'Student Name'
    student_name.admin_order_field = 'student__name' # Cho phép sort theo tên student

    # Nếu bạn muốn hiển thị student.grade thay vì attendance.class_id (nếu chúng có thể khác nhau)
    # def student_grade(self, obj):
    #     return obj.student.grade
    # student_grade.short_description = 'Actual Student Grade'