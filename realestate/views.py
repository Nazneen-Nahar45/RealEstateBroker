from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.contrib.sessions.models import  Session
# Create your views here.

def buy(request):
    return render(request,template_name='buy_features.html')

def rent(request):
    return render(request,template_name='rent_features.html')

def buyhome1(request):
    return render(request,template_name='b_feat_1.html')

def buyhome2(request):
    return render(request,template_name='b_feat_2.html')

def renthome1(request):
    return render(request,template_name='r_feat_1.html')

def renthome2(request):
    return render(request,template_name='r_feat_2.html')

def confirm(request):
    return render(request,template_name='confirm.html')

def agent_p(request):
    return render(request,template_name='CompanyProfile.html')

def profile(request):
    return render(request,template_name='profile.html')

def agent(request):
    return render(request,template_name='agent.html')

def firstpage(request):
    return render(request,template_name='Admin_User.html')

def user_sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username , email=email , password = password)

        request.session['signup_username']= username
        request.session['signup_email'] = email
        request.session['signup_password'] = password

        user = authenticate(request,username=username , password = password)

        if user is not None :
            auth_login(request,user)
            messages.success(request,'Successfulyy signed up!')
            return redirect('user_login')
    return render(request,template_name='User_Signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            auth_login(request,user)
            messages.success(request,'Successfulyy Logged In!')
            return redirect('user_home')

    return render(request,template_name='User_Login.html')

def user_home(request):
    return render(request,template_name='User_Home.html')

def user_sell(request):
    return render(request,template_name='Customer_Sell.html')


def agent_sign(request):
    return render(request,template_name='Admin_Signup.html')

def agent_login(request):
    return render(request,template_name='Admin_Login.html')

def agent_home(request):
    return render(request,template_name='agent_home.html')

def agent_sell(request):
    return render(request,template_name='Agent_Sell.html')

def faq(request):
    return render(request,template_name='FAQ.html')
