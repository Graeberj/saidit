# Generated by Django 3.2.8 on 2021-10-12 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_created']},
        ),
    ]