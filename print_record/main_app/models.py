from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# create staff model with general information

class Student(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    name= models.CharField(max_length=100)
    rollnum = models.IntegerField()
    printed_pages = models.IntegerField(default=0)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    date_hired = models.DateField()
    date_terminated = models.DateField()
    active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name




