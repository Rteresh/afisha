# Generated by Django 2.2.18 on 2021-11-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0002_concert_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=models.ImageField(blank=True, max_length=500, upload_to='concerts_images'),
        ),
    ]
