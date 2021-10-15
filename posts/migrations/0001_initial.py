# Generated by Django 3.2.8 on 2021-10-15 01:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=150)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.subgroup')),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
    ]
