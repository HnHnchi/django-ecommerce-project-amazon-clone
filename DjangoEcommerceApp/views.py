from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from DjangoEcommerceApp.models import CustomUser as User
from django.shortcuts import redirect




# Create your views here.
def createAccount(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("create_account")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("create_account")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used!")
            return redirect("create_account")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect("admin_login")

    return render(request, "create.html")
def home(request):
    return render(request, "demo.html")
def demoPage(request):
    return HttpResponse("demo Page")

def demoPageTemplate(request):
    return render(request,"demo.html")

def adminLogin(request):
    return render(request,"admin_templates/signin.html")

def adminLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("admin_login"))

def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successfully!")
    return HttpResponseRedirect(reverse("admin_login"))