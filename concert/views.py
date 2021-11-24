from django.shortcuts import render, HttpResponseRedirect
from concert.models import ClassicalMusic, OpenAir, Party, Concert, Basket


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
        'categories': [ClassicalMusic.__name__, OpenAir.__name__, Party.__name__],
        'products': Concert.objects.all()

    }
    return render(request, 'concerts/concerts.html', context)


def basket_add(request, concert_id):
    concert = Concert.objects.get(id=concert_id)
    baskets = Basket.objects.filter(user=request.user, concert=concert)
    current_page = request.META.get('HTTP_REFERER')
    if not baskets.exists():
        # basket = Basket(user=request.user, concert=concert, quantity_items_on_basket=1)
        # basket.save()
        Basket.objects.create(user=request.user, concert=concert, quantity_items_on_basket=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity_items_on_basket += 1
        basket.save()
        return HttpResponseRedirect(current_page)
