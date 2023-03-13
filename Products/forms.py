from django.forms import ModelForm 
from .models import ProductForCustomer

class Productaddform(ModelForm):
    class Meta:
        model = ProductForCustomer
        fields = ["Product_Name","Product_Category","Product_price","Product_Discription","Product_Stock","Product_Image"]