from django.urls import path
from contacts import views

app_name = 'contacts'
urlpatterns = [

    path('', views.contact, name ="contact")
]