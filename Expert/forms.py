from django.forms import ModelForm
from .models import FarmerProducts

class ProductAddform(ModelForm):
    class Meta:
        model = FarmerProducts
        fields = ["Product_Name","Product_Category","Product_price","Product_image","Product_stock"]
        
