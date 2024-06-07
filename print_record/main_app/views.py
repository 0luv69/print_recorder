from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *



def index(request):
    return HttpResponse("Hello, world. You're at the main_app index.")
