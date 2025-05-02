from django.contrib import admin

from .models import Category,Shirt
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(Category)
admin.site.register(Shirt)
admin.site.register(CustomUser, UserAdmin)