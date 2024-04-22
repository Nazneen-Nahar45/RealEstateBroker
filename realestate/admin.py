from django.contrib import admin
from .models import Sell
from .models import Agent
from .models import Rent

admin.site.register([Sell])
admin.site.register([Agent])
admin.site.register([Rent])