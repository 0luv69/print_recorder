#  add staff AIP

# Path: print_record/main_app/api.py

from rest_framework import viewsets


from .serializers import StaffSerializer

from .models import Staff
from rest_framework.response import Response

from rest_framework import status
from urllib import request
from rest_framework.views import APIView





class StaffApi(APIView):
    authentication_classes = []
    permission_classes = []

    
    def post(self, request):
        serializer = StaffSerializer(data=request.data)

        if serializer.is_valid():
            hospital = serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
 
            
            