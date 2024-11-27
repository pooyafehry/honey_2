from django.contrib import admin
from .models import User
from django.contrib import admin
from .models import CustomUser





@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display =['first_name','last_name','username','birthday','phone_number']


