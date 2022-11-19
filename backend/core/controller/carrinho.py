from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from core.models import Produto, Carrinho


def addcarrinho(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('produto_id'))
            produto_check = Produto.objects.get(id=prod_id)
            if (produto_check):
                if (Carrinho.objects.filter(user=request.user.id, produto_id=prod_id)):

                    return JsonResponse({'status': 'Produto já adicionado ao carrinho'})
                else:
                    prod_qtd = int(request.POST.get('produto_qtd'))

                    if produto_check.quantidade >= prod_qtd:
                        Carrinho.objects.create(
                            user=request.user, produto_id=prod_id, produto_qtd=prod_qtd)

                        return JsonResponse({'status': 'Produto adicionado com sucesso'})
                    else:
                        return JsonResponse({'status': 'Apenas '+str(produto_check.quantidade)+' disponível(is)'})

            else:
                return JsonResponse({'status': 'Produto não encontrado'})
        else:
            return JsonResponse({'status': 'Logue para continuar'})
    return redirect('home')


@login_required(login_url='loginpage')
def viewcarrinho(request):
    carrinho = Carrinho.objects.filter(user=request.user)  # type: ignore
    context = {'carrinho': carrinho}
    return render(request, 'loja/layout/carrinho.html', context)


def updatecarrinho(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('produto_id'))
        if (Carrinho.objects.filter(user=request.user, produto_id=prod_id)):
            prod_qtd = int(request.POST.get('produto_qtd'))
            carrinho = Carrinho.objects.get(
                produto_id=prod_id, user=request.user)
            carrinho.produto_qtd = prod_qtd
            carrinho.save()
            return JsonResponse({'status': 'Atualizado com sucesso'})
    return redirect('home')


def deletaritemcarrinho(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('produto_id'))
        if (Carrinho.objects.filter(user=request.user, produto_id=prod_id)):
            itemcarrinho = Carrinho.objects.get(
                produto_id=prod_id, user=request.user)
            itemcarrinho.delete()
            return JsonResponse({'status': 'Deletado com sucesso'})
    return redirect('home')
