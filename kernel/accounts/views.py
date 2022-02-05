from django.shortcuts import render, redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from contacts.models import Contact
from blog.models import *

def register(request):
    pages = Page.objects.filter(show_in_menu=True)
    socialmedia =Social.objects.all()
    contact=Contact_Us.objects.all()
    about=About.objects.all()
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username = username).exists():
                messages.error(request, 'این یوزر نیم از قبل وجود دارد')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'این ایمیل از قبل وجود دارد')
                    return redirect('accounts:register')

                else:
                    user = User.objects.create_user(username = username, password=password, email=email, first_name = first_name, last_name = last_name)
                    user.save()
                    messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
                    return render(request, 'accounts/login.html')

        else:
            messages.error(request, 'پسورد ها با هم یکی نیستن')
            return redirect('accounts:register')

    return render(request, 'accounts/register.html',{'socialmedia':socialmedia,'contact':contact, 'pages':pages, 'about':about})


def login(request):
    contact=Contact_Us.objects.all()
    about=About.objects.all()
    socialmedia =Social.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'شما وارد شده اید')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'نام کاربری یا پسورد نامعتبر است')
            return redirect ('accounts:login')
    else:
        return render(request, 'accounts/login.html',{'socialmedia':socialmedia, 'contact':contact, 'pages':pages, 'about':about })


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "شما با موفقیت خارج شده اید")
        return redirect('blog:home')


def dashboard(request):
    contact=Contact_Us.objects.all()
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    socialmedia =Social.objects.all()
    pages = Page.objects.filter(show_in_menu=True)
    about = About.objects.all()
    context = {
        'contacts':user_contacts,
        'socialmedia':socialmedia,
        'contact':contact,
        'pages':pages,
        'about':about
    }
    return render(request, 'accounts/dashboard.html', context)






