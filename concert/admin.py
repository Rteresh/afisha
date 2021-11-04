from django.contrib import admin
from concert.models import ClassicalMusic, OpenAir, Party

# Register your models here.
admin.site.register(ClassicalMusic)
admin.site.register(OpenAir)
admin.site.register(Party)
