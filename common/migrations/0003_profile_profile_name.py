# Generated by Django 3.2.8 on 2021-10-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
