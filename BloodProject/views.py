from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'BloodProject/index.html')

def service(request):
    return render(request, 'BloodProject/service.html')

def appointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        hour = request.POST.get('hour')
        plan = request.POST.get('plan')
        bloodty = request.POST.get('bloodty')
        send_mail(
            "confirmation mail",
            "Your Appointment Booked Successfully ",
            "EMAIL_HOST_USER",
            [email],
            fail_silently=False,
        )

    return render(request, 'BloodProject/appointment.html')



def blog(request):
    return render(request, 'BloodProject/blog.html')
def about(request):
    return render(request, 'BloodProject/about.html')



def handlesignup(request):
    if request.method == 'POST':
        # get the post parameter
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        Email = request.POST['email']

        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect("/")
        if password != confirm_password:
            messages.error(request, "password do not match")
            return redirect("/")

        if not username.isalnum():
            messages.error(request, "username only contain letters and numbers")
            return redirect("/")

        # create the user

        myuser = User.objects.create_user(username, Email, password)

        myuser.first_name = firstname
        myuser.last_name = lastname
        # To add other fields myuser.email=emailvariable
        myuser.save()

        messages.success(request, "Your account created succesfully")

        return redirect("BloodProject:login")

    else:
        return render(request, "BloodProject/signup.html")


def handlelogin(request):
    if request.method == 'POST':
        # get the post parameter

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logedin")
            return redirect("BloodProject:appointment")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/")

    return render(request, "BloodProject/login.html")

def handlelogut(request):
    logout(request)
    messages.success(request, "Successfuly logged Out")
    return redirect('/')