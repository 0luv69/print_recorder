from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.



class stdApi(APIView):
    def get(self, request):
        std_all_obj = Student.objects.all()
        std_ser_var = StdSerializer(std_all_obj, many=True)

        return Response({
            'payload' : std_ser_var.data,
            'Message': 'Success Fetched'
        },
        status=200)
    
    def post(self, request):
        data = request.data 
        std_ser_var = StdSerializer(data=data)

        if std_ser_var.is_valid():
            std_ser_var.save()
            return Response({
                    'payload' : std_ser_var.data,
                    'Message': 'Success Saved'
            }, status=200
            )
        return Response({ 'payload': std_ser_var.data, 'error': std_ser_var.errors }, status=403)

