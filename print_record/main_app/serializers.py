from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
        


class StdSerializer(serializers.ModelSerializer):
    user= UserSerializer()
    class Meta:
        model = Student
        fields= '__all__'