# announcements/admin.py

from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'time', 'created_at', 'updated_at')
    list_filter = ('category', 'date')
    search_fields = ('title', 'message', 'recipients') # Có thể tìm kiếm trong JSONField nếu DB hỗ trợ
    date_hierarchy = 'date' # Thêm thanh điều hướng theo ngày
    readonly_fields = ('created_at', 'updated_at') # Không cho phép chỉnh sửa thời gian tạo/cập nhật thủ công

    # Để recipients dễ đọc và chỉnh sửa trong Admin
    # Override formfield_for_dbfield để hiển thị JSONField như một textarea
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'recipients':
            kwargs['widget'] = admin.widgets.AdminTextareaWidget # Hoặc forms.CharField(widget=forms.Textarea)
        return super().formfield_for_dbfield(db_field, **kwargs)

    # Nếu bạn muốn hiển thị recipients dưới dạng chuỗi comma-separated trong list_display
    def get_recipients_display(self, obj):
        return ", ".join(obj.recipients) if obj.recipients else "None"
    get_recipients_display.short_description = 'Recipients'
    # Nếu dùng hàm này, nhớ thêm 'get_recipients_display' vào list_display