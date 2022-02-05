from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from blog.models import *


def index(request):
    listings = Listing.objects.order_by('-published_at')
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    socialmedia = Social.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    contact = Contact_Us.objects.all()
    about = About.objects.all()
    context = {
        'listings': page_listings,
        'socialmedia': socialmedia,
        'contact': contact,
        'pages': pages,
        'about': about
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    socialmedia = Social.objects.all()
    contact = Contact_Us.objects.all()
    about = About.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    context = {
        'listing': listing,
        'socialmedia': socialmedia,
        'contact': contact,
        'pages': pages,
        'about': about
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    pages = Page.objects.filter(show_in_menu=True)
    about = About.objects.all()
    contact = Contact_Us.objects.all()
    socialmedia = Social.objects.all()
    queryset_list = Listing.objects.order_by('-published_at')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
        'pages': pages,
        'about': about,
        'contact': contact,
        'socialmedia': socialmedia,
    }
    return render(request, 'listings/search.html', context)
