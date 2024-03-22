from django.shortcuts import render

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
    return render(request,template_name='User_Signup.html')

def user_login(request):
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
