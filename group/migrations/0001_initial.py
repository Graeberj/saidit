<<<<<<< HEAD
# Generated by Django 3.2.8 on 2021-10-17 17:46
=======
# Generated by Django 3.2.8 on 2021-10-17 19:44
>>>>>>> 40ce046e69d06efcb4c7aef28d443182781cecae

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('group_description', models.TextField(null=True)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
