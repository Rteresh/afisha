from django.db import models
from users.models import User
from django_resized import ResizedImageField


# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    quantity_tickets = models.PositiveIntegerField(default=100, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    post_image = ResizedImageField(size=[300, 300], upload_to='concerts_images', blank=True, null=True, max_length=500)

    def __str__(self):
        return self.name


class Voice(models.Model):
    type_of_voice = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.type_of_voice


class ClassicalMusic(Concert):
    type_of_voice = models.ForeignKey(Voice, on_delete=True)
    name_executor = models.CharField(max_length=64, unique=True)


class OpenAir(Concert):
    address = models.TextField(blank=False)
    headliner = models.CharField(blank=False, max_length=64)


class Party(Concert):
    age = models.PositiveIntegerField(blank=False)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    quantity_items_on_basket = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | {self.concert.name}'

    def sum(self):
        return self.quantity_items_on_basket * self.concert.price
