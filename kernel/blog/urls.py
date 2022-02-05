
from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
]