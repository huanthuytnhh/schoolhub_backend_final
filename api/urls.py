from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('chat/', include('chat.urls')),
    # Add this once we implement the announcements app
    # path('announcements/', include('announcements.urls')),
]
