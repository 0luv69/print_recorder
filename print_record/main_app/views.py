from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.

class stdApi(APIView):
    def get(self, request):
        std_all_obj = Student.objects.all()
        ser_std_var = StdSerializer(std_all_obj, many=True)

        return Response({
            'payload' : ser_std_var.data,
            'Message': 'Success Fetched'
        },
        status=200)
    
    def post(self, request):
        data = request.data 
        ser_std_var = StdSerializer(data=data)

        if ser_std_var.is_valid():
            ser_std_var.save()
            return Response({
                    'payload' : ser_std_var.data,
                    'Message': 'Success Saved'
            }, status=200
            )
        return Response({ 'payload': ser_std_var.data, 'error': ser_std_var.errors }, status=403)

    # # ?id=1
    def patch(self, request):
        id = request.GET.get('id')
        data = request.data 
        try:
            std_obj= Student.objects.get(id=id)
            ser_std_var= StdSerializer(std_obj, data=data, partial= True)
            if ser_std_var.is_valid():
                ser_std_var.save()
                return Response({'payload': data,'message': 'patch student success' }, status=200)
            return Response({'payload': data,'error reason' : ser_std_var.errors , 'message': 'Bad request here' }, status= 403,)
        except Exception as e:
            return Response({'error reason' : f'{e}' , 'message': 'hint: ID is not valid'}, status= 403)

                


