# Generated by Django 3.2.8 on 2021-10-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20211010_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
