# Generated by Django 2.1.5 on 2022-02-05 17:41

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_header', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('zipcode', models.CharField(blank=True, max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('bedrooms', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('garage', models.IntegerField(blank=True, default=0)),
                ('sqft', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('realtor', models.ManyToManyField(related_name='listing', to='realtors.Realtor')),
            ],
            options={
                'verbose_name': 'لیست',
                'verbose_name_plural': 'لیست',
            },
        ),
    ]