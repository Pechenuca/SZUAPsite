# Generated by Django 3.1.8 on 2022-04-13 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220411_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='label',
        ),
        migrations.RemoveField(
            model_name='carier',
            name='label',
        ),
    ]
