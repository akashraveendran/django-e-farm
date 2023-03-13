from django.db import models
from django.contrib.auth.models import User

class ProductForCustomer(models.Model):
    options = (
    ("Fruits","Fruits"),
    ("Vegetable","Vegetable"),
    ("other","other")
    )
    
    Product_Name = models.CharField(max_length=244)
    Product_Category = models.CharField(max_length=255,choices=options)
    Product_price = models.IntegerField()
    Product_Discription = models.CharField(max_length=1000)
    Product_Stock = models.IntegerField()
    Product_Image = models.FileField(upload_to="Customer_products")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    
class CustomerCheckout(models.Model):
    
    product = models.ForeignKey(ProductForCustomer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)
    Payment = models.BooleanField(default=False)
    