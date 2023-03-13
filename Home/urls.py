from django.urls import path 
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("FarmerHome",views.FarmerHome,name="FarmerHome"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("UserConfirmation",views.UserConfirmation,name="UserConfirmation"),
    path("UserGroupChange/<str:value>",views.UserGroupChange,name="UserGroupChange"),
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("ExpertAdd",views.ExpertAdd,name="ExpertAdd"),
    path("UserList",views.UserList,name="UserList"),
    path("ExpertHome",views.ExpertHome,name="ExpertHome"),
    
    
]
