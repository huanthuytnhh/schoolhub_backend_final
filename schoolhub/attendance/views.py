# attendance/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .models import Attendance, Student # Student từ app students
from .serializers import AttendanceSerializer
from django.db.models import Q

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    # queryset ban đầu có thể là rỗng hoặc tất cả, sẽ được ghi đè trong get_queryset
    queryset = Attendance.objects.all().select_related('student')


    def get_queryset(self):
        """
        Ghi đè để lọc dựa trên query parameters.
        - ?classId=xxx&date=YYYY-MM-DD : Lấy điểm danh của lớp theo ngày
        - ?studentId=xxx&month=MM&year=YYYY : Lấy lịch sử điểm danh của học sinh theo tháng/năm
        """
        queryset = super().get_queryset() # Lấy queryset gốc (Attendance.objects.all().select_related('student'))

        # Lấy tham số từ query params của request
        class_id_param = self.request.query_params.get('classId') # Lưu ý: Frontend gửi là classId
        date_str_param = self.request.query_params.get('date')

        student_id_param = self.request.query_params.get('studentId')
        month_param = self.request.query_params.get('month')
        year_param = self.request.query_params.get('year')

        # Lọc cho điểm danh theo lớp và ngày
        if class_id_param and date_str_param:
            attendance_date = parse_date(date_str_param)
            if attendance_date:
                # class_id trong model Attendance lưu trữ grade của học sinh
                queryset = queryset.filter(class_id=class_id_param, date=attendance_date)
            else:
                return Attendance.objects.none() # Ngày không hợp lệ
        # Lọc cho lịch sử điểm danh của học sinh
        elif student_id_param and month_param and year_param:
            try:
                student_id = int(student_id_param)
                month = int(month_param)
                year = int(year_param)
                queryset = queryset.filter(
                    student_id=student_id,
                    date__year=year,
                    date__month=month
                ).order_by('date') # Sắp xếp theo ngày cho lịch sử
            except ValueError:
                return Attendance.objects.none() # Tham số không hợp lệ
        else:
            # Nếu không có tham số lọc hợp lệ, không trả về gì cả để tránh tải toàn bộ dữ liệu
            # Hoặc bạn có thể bắt buộc phải có ít nhất một bộ filter
            return Attendance.objects.none()

        return queryset

    # perform_create và perform_update không cần ghi đè nếu logic upsert đã nằm trong serializer.create()
    # Nếu bạn muốn logic ở view:
    # def perform_create(self, serializer):
    #     student_id = self.request.data.get('studentId')
    #     class_id_from_payload = self.request.data.get('classId') # Đây là student.grade
    #     date_from_payload = self.request.data.get('date')
    #     # ... (lấy các trường khác)
    #     try:
    #         student = Student.objects.get(id=student_id)
    #     except Student.DoesNotExist:
    #         raise serializers.ValidationError({'student_id': 'Invalid student ID.'})

    #     # Logic upsert
    #     attendance_obj, created = Attendance.objects.update_or_create(
    #         student=student,
    #         date=parse_date(date_from_payload),
    #         defaults={
    #             'class_id': class_id_from_payload, # Lưu lại grade của student
    #             'is_present': self.request.data.get('isPresent'),
    #             'notes': self.request.data.get('notes')
    #         }
    #     )
    #     # serializer.save() sẽ không được gọi nếu bạn tự tạo object
    #     # Thay vào đó, bạn cần trả về Response với object đã serialize
    #     # Tuy nhiên, DRF sẽ tự gọi serializer.save() nếu bạn không ghi đè create() hoàn toàn
    #     # Cách đơn giản nhất là để serializer.create() xử lý upsert
    #     serializer.save(student_id=student_id) # Truyền student_id cho serializer

    # ModelViewSet đã hỗ trợ các phương thức:
    # list (GET /api/attendances/ -> có filter từ get_queryset)
    # create (POST /api/attendances/ -> sử dụng serializer.create để upsert)
    # retrieve (GET /api/attendances/{id}/)
    # update (PUT /api/attendances/{id}/)
    # destroy (DELETE /api/attendances/{id}/)
    # Frontend chủ yếu sẽ dùng 'list' (với params) và 'create'.