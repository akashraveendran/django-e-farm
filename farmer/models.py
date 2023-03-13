from django.db import models
from django.contrib.auth.models import User


class SeedFarm(models.Model):
    seedname = models.CharField(max_length=55)
    farmfield = models.CharField(max_length=55)
    framarea = models.CharField(max_length=55)
    framstatus = models.CharField(max_length=1000)
    image = models.FileField(upload_to="framimage")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
class FarmStatus(models.Model):
    Farm = models.ForeignKey(SeedFarm,on_delete=models.CASCADE)
    Expert = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Status = models.CharField(max_length=255)
    questions = models.CharField(max_length=1000,blank=True,null=True)
    answers = models.CharField(max_length=1000,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
     
