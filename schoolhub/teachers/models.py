# teachers/models.py

from django.db import models

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # Email should be unique for teachers
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    avatar = models.URLField(max_length=200, blank=True, null=True)
    classInCharge = models.CharField(max_length=10, blank=True, null=True) # Optional as a teacher might not be in charge of a class immediately
    dateOfBirth = models.DateField(blank=True, null=True)
    # WARNING: Storing passwords directly in a model is a security risk.
    # For real applications, use Django's built-in User model for authentication.
    password = models.CharField(max_length=128, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='teacher')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
