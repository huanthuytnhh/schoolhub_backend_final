from django.shortcuts import render

# Create your views here.
# menu/views.py

from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'