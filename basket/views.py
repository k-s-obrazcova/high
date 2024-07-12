from django.shortcuts import render

from basket.basket import Basket


# Create your views here.
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})
