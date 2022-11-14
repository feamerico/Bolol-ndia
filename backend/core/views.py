from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import ItemPadr, ItensPedidos, Pedido
from django.views.generic.edit import CreateView


def home(request):
    pedidos = Pedido.objects.all()
    itensdopedido = ItensPedidos.objects.all()  # type: ignore
    return render(request, 'home.html', {'pedidos': pedidos, 'itensdopedido': itensdopedido})


def itens(request):
    itens = ItemPadr.objects.all()
    return render(request, 'itens.html', {'itens': itens})


def pedidonovo(request):
    itens = ItemPadr.objects.all()
    return render(request, 'pedidonovo.html', {'itens': itens})


def pedidos(request):
    pedidos = Pedido.objects.all()
    itensdopedido = ItensPedidos.objects.all()  # type: ignore
    return render(request, 'pedidos.html', {'pedidos': pedidos, 'itensdopedido': itensdopedido})


def detalhesdopedido(request, id):
    pedidos = get_object_or_404(Pedido, id=id)
    itensdopedido = get_object_or_404(ItensPedidos, id=id)
    return render(request, 'detalhesdopedido.html', {'pedidos': pedidos, 'itensdopedido': itensdopedido})


class ItensPedidosCreateView(CreateView):
    model = ItensPedidos
    template_name = 'itenspedidos_form.html'
    fields = ['item', 'quantidade']
