from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from django.urls import reverse
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        contact = Contact(listing_id=listing_id, listing=listing, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'استعلام لیست املاک',
            'یک استعلام برای ' + listing + 'وجود دارد برای اظلاعات بیشتر وارد پنل ادمین شوید',
            'Amlak@gmail.com',
            [realtor_email, 'siyamak1981@gmail.com'],
            fail_silently=True

        )
        messages.success(request, 'message was successed')
        return redirect(reverse('listings:listings'))
