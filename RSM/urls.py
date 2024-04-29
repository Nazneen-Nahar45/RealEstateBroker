"""
URL configuration for RSM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from realestate import views as r_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',r_view.firstpage, name= 'firstpage'),
    path('user_sign/',r_view.user_sign,name = 'user_sign'),
    path('agent_sign/',r_view.agent_sign,name = 'agent_sign'),
    path('user_login/', r_view.user_login,name = 'user_login'),
    path('agent_login/' , r_view.agent_login, name='agent_login'),
    path('user_home/',r_view.user_home,name ='user_home'),
    path('user_sell/',r_view.user_sell,name='user_sell'),
    path('agent_sell/',r_view.agent_sell,name='agent_sell'),
    path('agent_home/',r_view.agent_home,name ='agent_home'),
    path('buy/',r_view.buy, name= 'buy'),
    path('rent/' ,r_view.rent, name='rent'),
    path('buyhome1/' ,r_view.buyhome1, name='buyhome1'),
    path('buyhome2/' ,r_view.buyhome2, name='buyhome2'),
    path('renthome1/' ,r_view.renthome1, name='renthome1'),
    path('renthome2/' ,r_view.renthome2, name='renthome2'),
    path('confirm/' ,r_view.confirm, name='confirm'),
    path('profile/' ,r_view.profile, name='profile'),
    path('agent/' ,r_view.agent, name='agent'),
    path('faq/',r_view.faq,name='faq'),
    path('addsell/',r_view.add_sell, name= 'add_sell'),
    path('addrent/',r_view.add_rent, name= 'add_rent'),
    path('logout_user/',r_view.logout_user, name= 'logout_user'),
    path('buy/<str:id>',r_view.property_details, name= 'property_details'),
    path('rent/<str:id>',r_view.property_details_rent, name= 'property_details_rent'),
    path('logout_agent/',r_view.logout_agent, name= 'logout_agent'),
    path('delete/<str:id>',r_view.delete_buy, name= 'delete_buy'),
    path('buy/<str:id>/confirm/',r_view.buy_confirm, name= 'buy_confirm'),
    path('rent/<str:id>/confirm/',r_view.rent_confirm, name= 'rent_confirm'),
    path('success/',r_view.success, name= 'success'),
    path('buy/<str:id>/con_buy/',r_view.con_buy, name= 'con_buy'),
    path('buy_list_agent/',r_view.buy_list_agent, name= 'buy_list_agent'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)