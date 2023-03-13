from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProductAddform
from .models import FarmerProducts,FramemerCheckout


def FarmersProducts(request):
    form  = ProductAddform()
    prod = FarmerProducts.objects.all()
    if request.method == "POST":
        form = ProductAddform(request.POST,request.FILES)
        if form.is_valid():
            val = form.save()
            val.user = request.user
            val.save()
            messages.info(request,"Product Added to List")
            return redirect(FarmersProducts)
    context = {
        "form":form,
        'products':prod
    }
    return render(request,'expert/products.html',context)

def DeleteFarmProducts(request,pk):
    FarmerProducts.objects.get(id = pk).delete()
    messages.info(request,"Product Deleted")
    return redirect('FarmersProducts')

def FramersOrder(request):
    orders = FramemerCheckout.objects.all()
    context = {
        "orders":orders
    }
    return render(request,'expert/farmersorder.html',context)

def AcceptOrder(request,pk):
    order = FramemerCheckout.objects.get(id = pk)
    order.status = "Order Accepted"
    order.save()
    return redirect("FramersOrder")

def DespachOrder(request,pk):
    order = FramemerCheckout.objects.get(id = pk)
    order.status = "Order Despached"
    order.save()
    return redirect("FramersOrder")

def RejectOrder(request,pk):
    order = FramemerCheckout.objects.get(id = pk)
    order.status = "Order Rejected"
    order.save()
    return redirect("FramersOrder")

def DeleteOrder(request,pk):
    FramemerCheckout.objects.get(id = pk).delete()
    messages.info(request,"item deleted")
    return redirect("FramersOrder")
    
    
    
