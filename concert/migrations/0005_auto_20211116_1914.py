# Generated by Django 2.2.18 on 2021-11-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0004_auto_20211116_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=models.ImageField(blank=True, max_length=500, upload_to='concerts_images'),
        ),
    ]
