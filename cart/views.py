from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, "cart/cart-summary.html", context)


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "cart-add":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        response = {"qty": cart.__len__()}
        return JsonResponse(response)


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "cart-delete":
        product_id = int(request.POST.get("product_id"))
        cart.delete(product=product_id)
        response = {"qty": cart.__len__(), "total": cart.get_total()}
        return JsonResponse(response)


def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "cart-update":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))
        cart.update(product=product_id, product_qty=product_quantity)
        response = {"qty": cart.__len__(), "total": cart.get_total()}
        return JsonResponse(response)
