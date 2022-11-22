from django.shortcuts import render

from core.models import PedidoItem, Pedido


def index(request):
    pedidos = Pedido.objects.filter(user=request.user)
    context = {'pedidos': pedidos}
    return render(request, 'loja/pedido/index.html', context)


def verpedido(request, id):
    pedido = Pedido.objects.filter(id=id).filter(user=request.user).first()
    itenspedido = PedidoItem.objects.filter(pedido=pedido)
    context = {"pedido": pedido, "itenspedido": itenspedido}
    return render(request, "loja/pedido/verpedido.html", context)
