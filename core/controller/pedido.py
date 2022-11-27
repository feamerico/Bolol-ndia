from django.shortcuts import render, redirect
from django.contrib import messages

from core.models import PedidoItem, Pedido


def index(request):
    if request.user.is_superuser:
        pedidos = Pedido.objects.all()
    else:
        pedidos = Pedido.objects.filter(user=request.user)
    context = {'pedidos': pedidos}
    return render(request, 'loja/pedido/index.html', context)


def verpedido(request, id):
    if Pedido.objects.filter(id=id).first():
        if request.user.is_superuser:
            pedido = Pedido.objects.filter(id=id).first()
        else:
            pedido = Pedido.objects.filter(
                id=id).filter(user=request.user).first()
        itenspedido = PedidoItem.objects.filter(pedido=pedido)
        context = {"pedido": pedido, "itenspedido": itenspedido}
        return render(request, "loja/pedido/verpedido.html", context)
    messages.warning(request, "Pedido não existe")
    return redirect('meuspedidos')
