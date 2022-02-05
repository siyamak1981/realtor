
from django.urls import path
from . import views
from accounts import views


app_name = 'accounts'
urlpatterns = [

    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),


]
