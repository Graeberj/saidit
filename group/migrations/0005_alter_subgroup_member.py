# Generated by Django 3.2.8 on 2021-10-11 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0004_subgroup_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroup',
            name='member',
            field=models.ManyToManyField(blank=True, related_name='group_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
