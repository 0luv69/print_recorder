from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    name= models.CharField(max_length=100)
    rollnum = models.IntegerField()
    printed_pages = models.IntegerField(default=0)


