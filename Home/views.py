from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from .decorators import admin_only,NullGroup
from django.http import HttpResponse
from farmer.models import FarmStatus
from Products.models import ProductForCustomer
from Expert.models import FarmerProducts


@admin_only
def Index(request):
    products = ProductForCustomer.objects.all()
    context = {
        "products":products
    }
    return render(request,"index.html",context)

def FarmerHome(request):
    products = FarmerProducts.objects.all()
    context = {
        "products":products
    }
    return render(request,'farmerhome.html',context)

def AdminHome(request):
    return render(request,"admin/adminhome.html")

def ExpertHome(request):
    Farm = FarmStatus.objects.all()
    context = {
        "farm":Farm
    }
    return render(request,'expert/expertHome.html',context)

def UserList(request):
    user = User.objects.all()
    return render(request,"admin/userslist.html",{"user":user})

@NullGroup
def UserConfirmation(request):
    return render(request,"userconfirmation.html")

def UserGroupChange(request,value):
    user = request.user
    if value == 'customer':
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        return redirect("Index")
        
    elif value == 'farmer':
        group = Group.objects.get(name='farmer')
        user.groups.add(group)
        return redirect("Index")
    
    return redirect("Index")

def ExpertAdd(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('ExpertAdd')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('ExpertAdd')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='expert')
                new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('ExpertAdd')
            
    return render(request,"admin/addexpert.html",{"form":form})
    
    

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('SignIn')
            
    return render(request,"register.html",{"form":form})



def SignOut(request):
    logout(request)
    return redirect('Index')

