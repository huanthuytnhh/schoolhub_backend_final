# teachers/admin.py

from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'classInCharge')
    search_fields = ('name', 'email', 'classInCharge')
    list_filter = ('gender', 'classInCharge')
