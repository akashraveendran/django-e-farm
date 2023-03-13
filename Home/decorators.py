from django.http import HttpResponse
from django.shortcuts import redirect


#decorator for user redirect...............
def unautenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('homescreen')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func

# allowed user decorators................
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

#decorators for user wise redirect pages...............
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == None:
                return redirect('UserConfirmation')
            
            if group == 'customer':
                return view_func(request, *args, **kwargs)
        
            if group == 'farmer':
                return redirect('FarmerHome')
            if group == 'admin':
                return redirect('AdminHome')
            if group == "expert":
                return redirect("ExpertHome")
        else:
            return view_func(request, *args, **kwargs)
            
    return wrapper_function

def NullGroup(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == None:
                return view_func(request,*args,**kwargs)
            else:
                return redirect("Index")
        else:
            return redirect("Index")
            
    return wrapper_func
            
            