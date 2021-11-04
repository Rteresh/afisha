from django.db import models


# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    quantity_tickets = models.PositiveIntegerField(default=100, blank=False)
    image = models.ImageField(upload_to='concerts_images', blank=True)


class Voice(models.Model):
    type_of_voice = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.type_of_voice


class ClassicalMusic(Concert):
    type_of_voice = models.ForeignKey(Voice, on_delete=True)
    name_executor = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class OpenAir(Concert):
    address = models.TextField(blank=False)
    headliner = models.CharField(blank=False, max_length=64)


class Party(Concert):
    age = models.PositiveIntegerField(blank=False)
