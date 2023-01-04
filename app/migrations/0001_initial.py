# Generated by Django 4.1.2 on 2022-12-27 15:18

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('heading', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=1000)),
                ('tex2', models.TextField(max_length=1000)),
                ('text3', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('name', models.CharField(max_length=100)),
                ('paragrapagh1', models.TextField(max_length=1000)),
                ('paragrapagh2', models.TextField(max_length=1000)),
                ('paragrapagh3', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('description', models.TextField(max_length=4000)),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
