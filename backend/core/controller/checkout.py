from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core.models import Carrinho, Loja, PedidoItem, Pedido, Produto, Perfil


@login_required(login_url='loginpage')
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

    userprofile = Perfil.objects.filter(user=request.user).first()

    context = {'cartitems': cartitems,
               'total_price': total_price, 'lojas': lojas, 'userprofile': userprofile}
    return render(request, "loja/layout/checkout.html", context)


@login_required(login_url='loginpage')  # type: ignore
def emitirpedido(request):
    if request.method == "POST":
        if Carrinho.objects.filter(user=request.user):
            currentuser = User.objects.filter(id=request.user.id).first()

            if not currentuser.first_name or not currentuser.last_name or not currentuser.email:
                currentuser.first_name = request.POST.get('nome')
                currentuser.last_name = request.POST.get('sobrenome')
                currentuser.email = request.POST.get('email')
                currentuser.save()

            if not Perfil.objects.filter(user_id=request.user.id):
                userprofile = Perfil()
                userprofile.user = request.user
                userprofile.telefone = request.POST.get('telefone')
                userprofile.loja = Loja.objects.filter(  # type: ignore
                    endereco=request.POST.get('loja')).first()
                userprofile.save()

            novopedido = Pedido()
            novopedido.user = request.user
            novopedido.nome = request.POST.get('nome')
            novopedido.sobrenome = request.POST.get('sobrenome')
            novopedido.email = request.POST.get('email')
            novopedido.telefone = request.POST.get('telefone')
            novopedido.loja = Loja.objects.filter(  # type: ignore
                endereco=request.POST.get('loja')).first()

            novopedido.forma_pagamento = request.POST.get('forma_pagamento')

            carrinho = Carrinho.objects.filter(user=request.user)
            carrinho_total_price = 0
            for item in carrinho:
                carrinho_total_price = carrinho_total_price + \
                    item.produto.valorvenda * item.produto_qtd  # type: ignore

            novopedido.total_price = carrinho_total_price

            novopedido.save()

            novopedidoitens = Carrinho.objects.filter(user=request.user)
            for item in novopedidoitens:
                PedidoItem.objects.create(
                    pedido=novopedido,
                    produto=item.produto,
                    valor=item.produto.valorvenda,
                    quantidade=item.produto_qtd
                )

                # redução dos itens do estoque
                produtopedido = Produto.objects.filter(
                    id=item.produto.id).first()
                produtopedido.quantidade = produtopedido.quantidade - item.produto_qtd
                produtopedido.save()

            # limpar carrinho do usuário
            Carrinho.objects.filter(user=request.user).delete()
            messages.success(request, "Pedido emitido com sucesso")
            return redirect('meuspedidos')

    return redirect('home')
