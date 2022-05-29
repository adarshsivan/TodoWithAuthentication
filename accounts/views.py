from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login as auth_login
# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']
        if pswd1 == pswd2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, password=pswd1, email=email)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Not Match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pswd = request.POST['pswd1']
        user = auth.authenticate(username=username, password=pswd)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            messages.info(
                request, "Wrong Credentials... Please check the Username and Password!!!")
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
