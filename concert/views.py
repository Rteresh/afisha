from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'tittle': 'Afisha'
    }
    return render(request, 'concerts/index.html', context)


def concerts(request):
    context = {

    }
    return render(request, 'concerts/concerts.html', context)
