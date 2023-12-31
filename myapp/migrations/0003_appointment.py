# Generated by Django 4.2.8 on 2023-12-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
