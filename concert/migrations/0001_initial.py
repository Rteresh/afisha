# Generated by Django 2.2.18 on 2021-11-04 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
                ('quantity_tickets', models.PositiveIntegerField(default=100)),
                ('image', models.ImageField(blank=True, upload_to='concerts_images')),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_voice', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenAir',
            fields=[
                ('concert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='concert.Concert')),
                ('address', models.TextField()),
                ('headliner', models.CharField(max_length=64)),
            ],
            bases=('concert.concert',),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('concert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='concert.Concert')),
                ('age', models.PositiveIntegerField()),
            ],
            bases=('concert.concert',),
        ),
        migrations.CreateModel(
            name='ClassicalMusic',
            fields=[
                ('concert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='concert.Concert')),
                ('name_executor', models.CharField(max_length=64, unique=True)),
                ('type_of_voice', models.ForeignKey(on_delete=True, to='concert.Voice')),
            ],
            bases=('concert.concert',),
        ),
    ]
