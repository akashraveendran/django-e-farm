from django.db import models
from django.contrib.auth.models import User 

class FarmerProducts(models.Model):
    options = (
        ("Fertilizer","Fertilizers"),
        ("Seeds","Seeds"),
        ("Accessories","Accessories")
    )
    
    Product_Name = models.CharField(max_length=255)
    Product_Category = models.CharField(max_length=255,choices=options)
    Product_price = models.IntegerField()
    Product_image = models.FileField(upload_to="farmer_product")
    Product_stock = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    status = models.BooleanField(default=True)
    
class FramemerCheckout(models.Model):
    
    product = models.ForeignKey(FarmerProducts,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)
    Payment = models.BooleanField(default=False)
    
