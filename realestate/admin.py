from django.contrib import admin
from .models import Sell
from .models import Agent

admin.site.register([Sell])
admin.site.register([Agent])