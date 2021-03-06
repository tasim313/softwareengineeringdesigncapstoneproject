# Generated by Django 3.1.3 on 2020-11-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Farmer', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=264)),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
                ('address_1', models.TextField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
