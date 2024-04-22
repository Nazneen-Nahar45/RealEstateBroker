from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.sessions.models import  Session
from .forms import *
from .models import Agent
from .models import Sell
from .models import Rent

# Create your views here.

def buy(request):
    buy_list=Sell.objects.all()
    context= {
        'buy_list': buy_list,
    }

    return render(request,template_name='buy_features.html', context=context )

def rent(request):
    rent_list=Rent.objects.all()
    context= {
        'rent_list': rent_list,
    }

    return render(request,template_name='rent_features.html', context=context )



def property_details(request, id):
    buy = Sell.objects.get(pk = id)
    context ={
        'buy': buy,
    }
    return render(request,template_name='property_details.html',context=context)


def property_details_rent(request, id):
    rent = Rent.objects.get(pk = id)
    context ={
        'rent': rent,
    }
    return render(request,template_name='property_details_rent.html',context=context)

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

def logout_user(request):
     logout(request)
     messages.success(request,'Youre logged out!')
     return redirect('user_login')

def user_home(request):
    return render(request,template_name='User_Home.html')

def user_sell(request):
    return render(request,template_name='Customer_Sell.html')



def add_sell(request):
    form = SellForm()
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agent_home')
    context ={
        'form':form,
    }
    return render(request,template_name='sell.html', context=context)

def add_rent(request):
    form = RentForm()
    if request.method == 'POST':
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agent_home')
    context ={
        'form':form,
    }
    return render(request,template_name='rent.html', context=context)


def agent_sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        password = request.POST.get('password')

        if name and email and company_name and password :
            new_agent = Agent(
                name = name,
                email = email,
                company_name= company_name,
                password = password
            )
            new_agent.save()

            request.session['agent_name'] =name
            request.session['agent_email'] = email
            request.session['agent_company_name'] = company_name
            request.session['agent_password'] = password

            return redirect('agent_login')
        else :
            messages.error(request,'Please fillup the form!')

            return redirect('agent_sign')

    return render(request,template_name='Admin_Signup.html')

def agent_login(request):
    if  request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Agent.objects.filter(name = name).exists():
            agent= Agent.objects.get(name= name)

            if agent.password==password :
               request.session['agent_name'] = agent.name
               request.session['agent_email'] = agent.email
               request.session['agent_company_name'] = agent.company_name
               request.session['agent_password'] = agent.password

               return redirect("agent_home")

            else :
                messages.error(request,'please fillup the form')

                return redirect('agent_login')

        else :
            messages.error(request,'invalid username!')

    return render(request,template_name='Admin_Login.html')

def agent_home(request):
    return render(request,template_name='agent_home.html')

def agent_sell(request):
    return render(request,template_name='Agent_Sell.html')

def faq(request):
    return render(request,template_name='FAQ.html')


def nav(request):
    try:
        user = User.objects.get(user=request.user)
    except Exception as e:
        user = None
        print('Exception : ', e)
    
    context = {'user': user,


               
        }

    return render(request,template_name='nav.html', ) 



def username_show(request):
    
    
    return render(request, 'navbar.html', {'username': username})