from django.contrib import admin
from .models import *
from khayyam import JalaliDate as jd


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo']
    list_filter = ('title','menu_title', 'menu_title1', 'menu_title2')


@admin.register(Subfooter)
class SubfooterAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title']
   
    list_filter = ('icon','title',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['url', 'png']
    list_filter = ('url',)
  
    
  
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title']
    list_filter = ('title',)
  
    
@admin.register(Contact_Us)
class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone']
    list_filter = ('email', 'phone')
    
  




  


    

