from django.urls import path

from .views import get_stream_token

urlpatterns = [
    path("stream-token/", get_stream_token, name="stream-token"),
]
