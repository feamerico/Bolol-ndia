from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Categoria, Produto


def home(request):
    return render(request, 'loja/layout/index.html')


def categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'loja/layout/categorias.html', context=context)


def produtos(request, slug):
    if (Categoria.objects.filter(slug=slug)):
        produtos = Produto.objects.filter(Categoria__slug=slug)
        categoria_nome = Categoria.objects.filter(slug=slug).first()
        context = {'produtos': produtos, 'categoria_nome': categoria_nome}
        return render(request, 'loja/produtos/index.html', context=context)
    else:
        messages.warning(request, "Categoria não encontrada")
        return redirect('categorias')


def produto(request, categoria_slug, produto_slug):
    if (Categoria.objects.filter(slug=categoria_slug)):
        if (Produto.objects.filter(slug=produto_slug)):
            produto = Produto.objects.filter(slug=produto_slug).first()
            context = {'produto': produto}
        else:
            messages.error(request, "Produto não encontrado")
            return redirect('categorias')
    else:
        messages.error(request, "Categoria não encontrada")
        return redirect('categorias')
    return render(request, 'loja/produtos/detalheproduto.html', context=context)


def pedidonovo(request):
    itens = Produto.objects.all()
    return render(request, 'pedidonovo.html', {'itens': itens})


# def pedidos(request):
#     #pedidos = Pedido.objects.all()
#     itensdopedido = ItensPedidos.objects.all()  # type: ignore
#     return render(request, 'pedidos.html', {'pedidos': pedidos, 'itensdopedido': itensdopedido})


# def detalhesdopedido(request, id):
#     #pedidos = get_object_or_404(Pedido, id=id)
#     #itensdopedido = get_object_or_404(ItensPedidos, id=id)
#     # return render(request, 'detalhesdopedido.html', {'pedidos': pedidos, 'itensdopedido': itensdopedido})
