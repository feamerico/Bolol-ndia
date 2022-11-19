from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from core.models import Carrinho, Loja


def index(request):
    rawcart = Carrinho.objects.filter(user=request.user)
    for item in rawcart:
        if item.produto_qtd > item.produto.quantidade:
            Carrinho.objects.filter(id=item.id).delete()  # type: ignore

    cartitems = Carrinho.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.produto.valorvenda * item.produto_qtd

    lojas = Loja.objects.filter(fechado=False)

    context = {'cartitems': cartitems,
               'total_price': total_price, 'lojas': lojas}
    return render(request, "loja/layout/checkout.html", context)
