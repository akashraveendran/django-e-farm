from django.urls import path
from .import views

urlpatterns = [
    path("ProductAdd",views.ProductAdd,name="ProductAdd"),
    path("DeleteCustomerProduct/<int:pk>",views.DeleteCustomerProduct,name="DeleteCustomerProduct"),
    path("ProductSingleViewCustomer/<int:pk>",views.ProductSingleViewCustomer,name="ProductSingleViewCustomer"),
    path("CustomerMybooking",views.CustomerMybooking,name="CustomerMybooking"), 
    path("AllProducts",views.AllProducts,name="AllProducts"),
    path("CancelOrderCustomer/<int:pk>",views.CancelOrderCustomer,name="CancelOrderCustomer"),
    path("DeleteOrderCustomer/<int:pk>",views.DeleteOrderCustomer,name="DeleteOrderCustomer"),
    path("CustomerOrderFarmerview",views.CustomerOrderFarmerview,name="CustomerOrderFarmerview"),
    path("AcceptOrderCustomer/<int:pk>",views.AcceptOrderCustomer,name="AcceptOrderCustomer"),
    path("DespachOrderCustomer/<int:pk>",views.DespachOrderCustomer,name="DespachOrderCustomer"),
    path("RejectOrderCustomer/<int:pk>",views.RejectOrderCustomer,name="RejectOrderCustomer"),
    path("DeleteOrderCustomer/<int:pk>",views.DeleteOrderCustomer,name="DeleteOrderCustomer"),
    
          
    
]
