from django.shortcuts import render,redirect
from django.contrib import messages
from .models import SeedFarm,FarmStatus
from Expert.models import FarmerProducts
from Home.models import UserData
from Expert.models import FramemerCheckout


def StartFarm(request):
    farm = SeedFarm.objects.filter(user = request.user)
    farmstatus = []
    for i in farm:
        fm = FarmStatus.objects.filter(Farm = i)
    
    context = {
        "farm":farm,
        # "farmstatus":fm
        
    }
    return render(request,"farmer/startfarm.html",context)

def AddNewSeedFarm(request):
    if request.method == "POST":
        name = request.POST["seed"]
        field = request.POST["farmfields"]
        area = request.POST["area"]
        status = request.POST["status"]
        img = request.FILES["img"]
        
        farm = SeedFarm.objects.create(seedname=name,farmfield=field,framarea=area,framstatus=status,image=img,user=request.user)
        farm.save()
        messages.info(request,"New Seed Farm Created")
        return redirect('StartFarm')
    return redirect('StartFarm')

def FramStatusUpdate(request,pk):
    Farm = SeedFarm.objects.filter(id = pk)
    farm = SeedFarm.objects.get(id = pk)
    if request.method == "POST":
        status = request.POST["status"]
        questions = request.POST['questions']
        FarmStatus.objects.create(Farm=farm,Status=status,questions=questions).save()
        farm.framstatus = status
        farm.save()
        messages.info(request,"Status Updated")   
    
    farmstatus = FarmStatus.objects.filter(Farm = farm) 
    
    context = {
        "Farm":Farm,
        "farmstatus":farmstatus
    }
    return render(request,'farmer/farmstatusupdate.html',context)

def DeleteOpinion(request,pk,hk):
    FarmStatus.objects.get(id =pk).delete()
    messages.info(request,"item deleted")
    return redirect('FramStatusUpdate',pk = hk)

def UpdateAnswer(request,pk):
    farmstatus = FarmStatus.objects.get(id = pk)
    if request.method == "POST":
        ans = request.POST['ans']
        farmstatus.answers = ans
        farmstatus.save()
        return redirect("ExpertHome")
        
    return redirect("ExpertHome")

def FarmProducts(request):
    products = FarmerProducts.objects.all()
    context = {
        "products":products
    }
    return render(request,'farmer/productforfarm.html',context)

def FarmerMybooking(request):
    product = FramemerCheckout.objects.filter(user = request.user)
    return render(request,"farmer/mybooking.html",{'product':product})

def ProductSignleView(request,pk):
    product = FarmerProducts.objects.filter(id = pk)
    # form = UserDetailsForm()
    userdata1 = UserData.objects.filter(user = request.user)
    
    product1 = FarmerProducts.objects.get(id = pk)
    
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
        
        checkout = FramemerCheckout.objects.create(product = product1 ,user = request.user,status = "Customer Ordered")
        checkout.save()
        return redirect("FarmerMybooking")
        
    context = {
        "product":product,
        "userdata1":userdata1,
        "datalen":len(userdata1)
        # "form":form
        
    }
    return render(request,"farmer/farmerproductview.html",context)

def CancelOrderFarmer(request,pk):
    FRCKOT = FramemerCheckout.objects.get(id = pk)
    FRCKOT.status = "Cancelled By User"
    FRCKOT.save()
    messages.info(request,"Item Cancelled")
    return redirect("FarmerMybooking")

def DeleteOrderFarmer(request,pk):
    FramemerCheckout.objects.get(id = pk).delete()
    messages.info(request,"Item Deleted")
    return redirect("FarmerMybooking")
    
    
def MyProducts(request):
    return render(request,"farmer/myproducts.html")




