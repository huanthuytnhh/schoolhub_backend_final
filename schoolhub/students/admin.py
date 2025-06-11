# students/admin.py

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollNumber', 'grade', 'isPresent', 'gender', 'email', 'phoneNumber')
    search_fields = ('name', 'rollNumber', 'grade', 'email')
    list_filter = ('grade', 'isPresent', 'gender')
    # Fields that are optional can be set to None in list_display if you don't want them always visible
    # For example, if you want to see avatar, dateOfBirth, password:
    # list_display = ('name', 'rollNumber', 'grade', 'isPresent', 'gender', 'email', 'phoneNumber', 'avatar', 'dateOfBirth', 'password')
