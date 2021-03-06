# Generated by Django 2.1.5 on 2022-02-05 17:41

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('description', ckeditor.fields.RichTextField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'دلال فروش',
                'verbose_name_plural': 'دلال فروش',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'نقش',
                'verbose_name_plural': 'نقش',
            },
        ),
        migrations.AddField(
            model_name='realtor',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='realtor', to='realtors.Role'),
        ),
    ]
