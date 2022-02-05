from django.db import models
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from blog.models import *


class Social(models.Model):
    url = models.URLField(max_length=250)
    icon = IconField()
    png = models.ImageField(upload_to='png/%Y/%m/%d', blank=True)

      
    class Meta: 
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural ='شبکه اجتماعی'

    def __str__(self):
        return self.url


class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    menu_title = models.CharField(max_length=200)
    menu_title1 = models.CharField(max_length=200)
    menu_title2 = models.CharField(max_length=200)

    title = models.CharField(max_length=200)
    page_title = models.CharField(max_length=200)
    card_title = models.CharField(max_length=200)
    show_in_menu = models.BooleanField(default=False)
    logo = models.ImageField(
        upload_to='logo/%Y/%m/%d', blank=True)
    social = models.ManyToManyField('Social', related_name='page')
    publish = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

      
    class Meta: 
        verbose_name = 'صفحات'
        verbose_name_plural ='صفحات'

    def __str__(self):
        return self.title


class Subfooter(models.Model):
    icon = IconField()
    title = models.CharField(max_length=200)
    body = RichTextField()
      
    class Meta: 
        verbose_name = 'خدمات ما'
        verbose_name_plural ='خدمات ما'

    def __str__(self):
        return self.title


class About(models.Model):
    sub_title = models.CharField(max_length=200)
    page_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photo_about/%Y/%m/%d', blank=True)
    body = RichTextField()
    work_title = models.CharField(max_length=200)
    summary_work = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.sub_title


class Contact_Us(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    summary = models.CharField(max_length=200)
    icon1 = IconField()
    icon2 = IconField()

    class Meta: 
        verbose_name = 'تماس با ما'
        verbose_name_plural ='تماس با ما'

    def __str__(self):
        return self.title
