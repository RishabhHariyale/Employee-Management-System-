from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.success(request,"Username already Exits")
                return redirect ("/accounts/login/#")

            elif User.objects.filter(email = email).exists():
                messages.success(request , "Email Already Taken!!")
                return redirect ("/accounts/login/#")

            else:
                user = User.objects.create_user(username = username , email = email , password = password2)
                user.save()
                
                return redirect("/")

        else:
            messages.warning(request , "Password is not matching!!")
            return redirect("login")

        return redirect ("/")


    else:
        return render(request , "login.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username , password = password)
        if user is not None:
            auth_login(request , user)
            return redirect("/")
        else:
            messages.error(request , "Invalid Username or Password")
            return redirect("login")
    else:
        return render (request , "login.html")

def logout(request):
    auth_logout(request)
    return redirect ("/")