from django.contrib import admin
from .models import *

admin.site.register([Sell])
admin.site.register([Agent])
admin.site.register([Rent])
admin.site.register([Buyer])
admin.site.register([Renter])