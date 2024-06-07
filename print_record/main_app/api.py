#  add staff AIP

# Path: print_record/main_app/api.py

from .serializers import StaffSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *




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




class StaffApi(APIView):
    authentication_classes = []
    permission_classes = []

    
    def post(self, request):
        serializer = StaffSerializer(data=request.data)

        if serializer.is_valid():
            hospital = serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
 
            
            