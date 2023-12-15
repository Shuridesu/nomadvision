# Generated by Django 5.0 on 2023-12-15 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meta_description', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(default='', max_length=500)),
                ('title_image', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('title_image_description', models.CharField(default='', max_length=500)),
                ('subtitle', models.CharField(default='', max_length=255)),
                ('heading1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image1', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image1_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content1', models.TextField(blank=True, default='', null=True)),
                ('heading2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image2_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content2', models.TextField(blank=True, default='', null=True)),
                ('heading3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image3_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content3', models.TextField(blank=True, default='', null=True)),
                ('heading4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image4_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content4', models.TextField(blank=True, default='', null=True)),
                ('heading5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image5_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content5', models.TextField(blank=True, default='', null=True)),
                ('heading6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image6', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image6_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content6', models.TextField(blank=True, default='', null=True)),
                ('heading7', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image7', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image7_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content7', models.TextField(blank=True, default='', null=True)),
                ('heading8', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image8', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image8_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content8', models.TextField(blank=True, default='', null=True)),
                ('heading9', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image9', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image9_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content9', models.TextField(blank=True, default='', null=True)),
                ('heading10', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image10', models.ImageField(blank=True, default='', null=True, upload_to='post_images/')),
                ('image10_description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content10', models.TextField(blank=True, default='', null=True)),
                ('pub_date', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('is_recommended', models.BooleanField(default=False)),
                ('is_trends_ai', models.BooleanField(default=False)),
                ('is_trends_data', models.BooleanField(default=False)),
                ('is_industry_insights', models.BooleanField(default=False)),
                ('is_ai_software', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nomadApp.author')),
                ('category', models.ManyToManyField(blank=True, to='nomadApp.category')),
            ],
        ),
    ]