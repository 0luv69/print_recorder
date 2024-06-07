from rest_framework import serializers
from .models import*



class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        
        # create function here

    
    def create(self, validated_data):
        staff, created = Staff.objects.update_or_create(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            email=validated_data.pop('email'),
            phone=validated_data.pop('phone'),
            address=validated_data.pop('address'),
            city=validated_data.pop('city'),
            state=validated_data.pop('state'),
            zip_code=validated_data.pop('zip_code'),
            country=validated_data.pop('country'),
            date_hired=validated_data.pop('date_hired'),
            date_terminated=validated_data.pop('date_terminated'),
            active=validated_data.pop('active')
        )
        return staff