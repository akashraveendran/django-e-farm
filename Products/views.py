from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Productaddform
from .models import ProductForCustomer,CustomerCheckout
from Home.models import UserData
from django.contrib.auth.decorators import login_required

@login_required(login_url="SignIn")
def ProductAdd(request):
    form = Productaddform
    products = ProductForCustomer.objects.filter(user = request.user)
    if request.method == "POST":
        form = Productaddform(request.POST,request.FILES)
        if form.is_valid():
            prod = form.save()
            prod.user = request.user
            prod.save()
            messages.info(request,"Product added to list")
            return redirect('ProductAdd')
    context = {
        "form":form,
        "products":products
    }
    return render(request,'farmer/myproducts.html',context)

@login_required(login_url="SignIn")
def DeleteCustomerProduct(request,pk):
    ProductForCustomer.objects.get(id = pk).delete()
    messages.info(request,"Item Deleted")
    return redirect('ProductAdd')

@login_required(login_url="SignIn")
def ProductSingleViewCustomer(request,pk):
    product = ProductForCustomer.objects.filter(id = pk)
    product1 = ProductForCustomer.objects.get(id = pk)
    userdata1 = UserData.objects.filter(user = request.user)
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        state = request.POST["state"]
        house = request.POST["house"]
        
        if UserData.objects.filter(user = request.user).exists():
            userdata = UserData.objects.get(user = request.user)
            userdata1 = UserData.objects.filter(user = request.user)
            
            userdata.name = name
            userdata.phone = phone
            userdata.city = city
            userdata.state = state
            userdata.house = house
            userdata.save()
        else:
            userdata = UserData.objects.create(name = name, house = house,phone = phone,city = city,state = state,user = request.user)
            userdata.save()
        
        checkout = CustomerCheckout.objects.create(product = product1 ,user = request.user,status = "Customer Ordered")
        checkout.save()
        return redirect("CustomerMybooking")
    
    context = {
        "product":product,
        "userdata1":userdata1,
        "datalen":len(userdata1)
        
    }
    return render(request,'productview.html',context)

@login_required(login_url="SignIn")
def CustomerMybooking(request):
    product = CustomerCheckout.objects.filter(user = request.user)
    context = {
       "product":product 
    }
    return render(request,"customerorder.html",context)



@login_required(login_url="SignIn")
def AllProducts(request):
    products = ProductForCustomer.objects.all()
    context = {
        "products":products
    }
    return render(request,"products.html",context)

@login_required(login_url="SignIn")
def CancelOrderCustomer(request,pk):
    FRCKOT = CustomerCheckout.objects.get(id = pk)
    FRCKOT.status = "Cancelled By User"
    FRCKOT.save()
    messages.info(request,"Item Cancelled")
    return redirect("CustomerMybooking")

@login_required(login_url="SignIn")
def DeleteOrderCustomer(request,pk):
    CustomerCheckout.objects.get(id = pk).delete()
    messages.info(request,"Item Deleted")
    return redirect("CustomerMybooking")

def CustomerOrderFarmerview(request):
    print(request.user.id)
    orders = CustomerCheckout.objects.all()
    context = {"orders":orders}
    return render(request,"farmer/customerordersfarmerview.html",context)


def AcceptOrderCustomer(request,pk):
    order = CustomerCheckout.objects.get(id = pk)
    order.status = "Order Accepted"
    order.save()
    return redirect("CustomerOrderFarmerview")

def DespachOrderCustomer(request,pk):
    order = CustomerCheckout.objects.get(id = pk)
    order.status = "Order Despached"
    order.save()
    return redirect("CustomerOrderFarmerview")

def RejectOrderCustomer(request,pk):
    order = CustomerCheckout.objects.get(id = pk)
    order.status = "Order Rejected"
    order.save()
    return redirect("CustomerOrderFarmerview")

def DeleteOrderCustomer(request,pk):
    CustomerCheckout.objects.get(id = pk).delete()
    messages.info(request,"item deleted")
    return redirect("CustomerOrderFarmerview")