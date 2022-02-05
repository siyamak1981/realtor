from django.db import models
from datetime import datetime
from realtors.models import Realtor,Role
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Listing(models.Model):
    title_header=models.CharField(max_length=200)
    summary =models.CharField(max_length=200)
    realtor = models.ManyToManyField(Realtor,  related_name='listing')
    title = models.CharField(max_length=200)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    description = RichTextField()
    price = models.DecimalField(max_digits= 20, decimal_places=2, blank=True)
    bedrooms = models.IntegerField()
    bathroom = models.IntegerField()
    garage = models.IntegerField(default=0, blank=True)
    sqft = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_2= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_3= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_4= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_5= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_6= models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    published_at = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: 
        verbose_name = 'لیست'
        verbose_name_plural ='لیست'
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listings:listing', args=[ self.id])