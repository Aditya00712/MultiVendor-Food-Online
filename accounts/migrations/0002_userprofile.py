# Generated by Django 5.1.3 on 2024-11-10 05:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_pictures/')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='users/cover_pictures/')),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
