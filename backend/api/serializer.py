from rest_framework import serializers
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty
        fields = ('id','Name','Designation','About','Qualification','Email','Phone')
    
class DeparthmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = departhment
        fields = ('id','Name','HOD','About','staff')