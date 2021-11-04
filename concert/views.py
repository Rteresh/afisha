from django.shortcuts import render
from concert.models import Concert, ClassicalMusic, OpenAir, Party


# Create your views here.
def index(request):
    context = {
        'tittle': 'Afisha',
        'name': 'roma'
    }
    return render(request, 'concerts/index.html', context)


def concerts(request):
    context = {
        'tittle': 'test',
        'categories': [ClassicalMusic.__name__,OpenAir.__name__,Party.__name__],
    }
    return render(request, 'concerts/concerts.html', context)
