from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    name = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
