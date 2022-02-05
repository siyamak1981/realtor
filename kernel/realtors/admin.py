from django.contrib import admin
from .models import Realtor, Role
from realtors.models import *


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'degree']

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'phone', 'email', 'is_mvp' ]
    list_filter = ('name', 'hire_date', 'email')
    search_fields= ('name','role',)
    list_per_page =10


   