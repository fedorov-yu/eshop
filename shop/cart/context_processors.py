from django.http import HttpResponse
from django.shortcuts import render

from cart.cart import Cart


def cart(request):
    carts = Cart(request)
    return {'cart': carts}
