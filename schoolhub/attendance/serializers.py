# attendance/serializers.py
from rest_framework import serializers
from .models import Attendance
from students.models import Student # Import Student model

class AttendanceSerializer(serializers.ModelSerializer):
    # Để nhận studentId từ frontend khi POST/PUT
    # Frontend sẽ gửi studentId, không phải object student lồng nhau
    student_id = serializers.IntegerField(write_only=True)
    # class_id là CharField, sẽ được xử lý tự động từ payload khi POST/PUT
    # Khi GET, nó sẽ là giá trị từ model

    # Để trả về student_id khi GET (nếu không muốn trả về object student đầy đủ)
    # sử dụng student_id_prop từ model
    studentId = serializers.IntegerField(source='student_id_prop', read_only=True)
    # Hoặc nếu bạn muốn trả về thông tin student cơ bản:
    # student_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Attendance
        # fields bao gồm cả các trường bạn muốn trả về (read) và nhận vào (write)
        fields = ['id', 'student_id', 'studentId', 'class_id', 'date', 'is_present', 'notes']
        read_only_fields = ['id', 'studentId'] # 'studentId' là read-only vì nó lấy từ source

    # def get_student_info(self, obj):
    #     return {
    #         "id": obj.student.id,
    #         "name": obj.student.name,
    #         "grade": obj.student.grade
    #     }

    def validate_student_id(self, value):
        """Kiểm tra xem student_id có tồn tại không khi ghi."""
        if not Student.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Student with id {value} does not exist.")
        return value

    def validate_class_id(self, value):
        """Kiểm tra class_id không rỗng khi ghi."""
        if not value:
            raise serializers.ValidationError("class_id (representing student's grade) cannot be empty.")
        return value

    def create(self, validated_data):
        student_id_val = validated_data.pop('student_id')
        student_instance = Student.objects.get(id=student_id_val)

        # class_id đã có trong validated_data từ payload
        # Logic Upsert:
        attendance_instance, created = Attendance.objects.update_or_create(
            student=student_instance,
            date=validated_data.get('date'),
            defaults={
                'class_id': validated_data.get('class_id'),
                'is_present': validated_data.get('is_present'),
                'notes': validated_data.get('notes', None) # Dùng None nếu không có
            }
        )
        return attendance_instance

    def update(self, instance, validated_data):
        # Khi PUT vào /api/attendances/{id}/
        # Frontend thường không dùng PUT trực tiếp vào record điểm danh,
        # mà sẽ POST lại với dữ liệu mới (đã được xử lý bởi upsert trong create)
        # Nhưng nếu bạn cho phép PUT, thì đây là cách cập nhật:
        instance.is_present = validated_data.get('is_present', instance.is_present)
        instance.notes = validated_data.get('notes', instance.notes)
        # Thông thường không cho phép thay đổi student, date, class_id của một record đã tồn tại qua PUT.
        instance.save()
        return instance