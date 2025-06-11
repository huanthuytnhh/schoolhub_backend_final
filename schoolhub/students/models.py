# students/models.py

from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    rollNumber = models.CharField(max_length=20, unique=True)
    isPresent = models.BooleanField(default=True)
    avatar = models.URLField(max_length=200, blank=True, null=True) # URL for avatar image
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True, blank=True, null=True)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    # WARNING: Storing passwords directly in a model is a security risk.
    # For real applications, use Django's built-in User model for authentication.
    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.rollNumber})"

    class Meta:
        ordering = ['rollNumber'] # Order students by roll number by default

