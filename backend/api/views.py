from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializer import *

class FacultyListCreate(ListCreateAPIView):
    queryset = faculty.objects.all()
    serializer_class = FacultySerializer

class DeparthmentListCreate(ListCreateAPIView):
    queryset = departhment.objects.all()
    serializer_class = DeparthmentSerializer