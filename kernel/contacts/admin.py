from django.contrib import admin
from . import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date' )
    list_display_link = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page =25


