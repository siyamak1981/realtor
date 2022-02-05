from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Role(models.Model):
    title = models.CharField(max_length=200)
    degree = models.CharField(max_length = 128)

    class Meta: 
        verbose_name = 'نقش'
        verbose_name_plural ='نقش'

    def __str__(self):
            return self.degree


class Realtor(models.Model):
    name = models.CharField(max_length = 128)
    photo = models.ImageField(upload_to ='photos/%Y/%m/%d', blank=True)
    description = RichTextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    is_mvp =models.BooleanField(default =False)
    hire_date = models.DateTimeField(default=datetime.now, blank = True)
    role = models.ForeignKey('Role', on_delete = models.DO_NOTHING, related_name= 'realtor')
    

    class Meta: 
        verbose_name = 'دلال فروش'
        verbose_name_plural ='دلال فروش'

    def __str__(self):
        return self.name