from django.contrib import admin
from khayyam import JalaliDate as jd
from .models import *
from realtors.models import Realtor, Role

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'price','get_realtors']
    list_filter = ('published_at', 'city',)
    search_fields = ('city', 'title')

    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title', 'city', 'price'), 
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'title_header',
                    'summary',
                    'photo_main',
                    'description',
                    'zipcode',
                    'address',
                    'bedrooms',
                    'bathroom',
                    'garage',
                    'sqft',
                    'state',
                    'photo_1',
                    'photo_2',
                    'photo_3',
                    'photo_4',
                    'photo_5',
                    'photo_6',
                    'published_at',
                    'realtor',
                  
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def published(self, obj):
        return jd(obj.published_at)

    def get_realtors(self, obj):
        return ", ".join([t.name for t in obj.realtor.all()])

    def is_published(self, obj):
        published = 1
        return obj.status == published
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []

    is_published.boolean = True


    def created_at(self, obj):
        return jd(obj.created)
    
    def updated_at(self, obj):
        return jd(obj.updated)

