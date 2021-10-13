# Generated by Django 3.2.8 on 2021-10-13 01:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saidituser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidituser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
