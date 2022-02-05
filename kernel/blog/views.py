
from django.shortcuts import render
from listings.models import *
from django.http import HttpResponse
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
from blog.models import *


def home(request):
    listings = Listing.objects.order_by('-published_at')[:3]
    socialmedia = Social.objects.all()
    contact = Contact_Us.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    subfooter = Subfooter.objects.all()
    about = About.objects.all()
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'socialmedia': socialmedia,
        'contact': contact,
        'pages': pages,
        'subfooter': subfooter,
        'about': about

    }
    return render(request, 'blog/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    about = About.objects.all()
    socialmedia = Social.objects.all()
    contact = Contact_Us.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'about': about,
        'socialmedia': socialmedia,
        'contact': contact,
        'pages': pages
    }

    return render(request, 'blog/about.html', context)
