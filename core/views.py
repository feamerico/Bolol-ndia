from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Categoria, Produto, PedidoItem


def home(request):
    produtos_mais_vendidos = PedidoItem.objects.raw('SELECT 1 as id, "core_pedidoitem"."produto_id", "core_categoria"."slug", "core_produto"."slug", "core_produto"."produto_imagem", "core_produto"."valorvenda", "core_produto"."nome", SUM("core_pedidoitem"."quantidade") AS "vendidos" FROM "core_pedidoitem" INNER JOIN "core_produto" ON ("core_pedidoitem"."produto_id" = "core_produto"."id") INNER JOIN "core_categoria" ON ("core_produto"."Categoria_id" = "core_categoria"."id") WHERE NOT ("core_categoria"."nome" = "Bebidas") GROUP BY "core_pedidoitem"."produto_id" ORDER BY "vendidos" DESC LIMIT 10')
    context = {'produtos_mais_vendidos': produtos_mais_vendidos}
    return render(request, 'loja/layout/index.html', context)


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


def listaprodutosAjax(request):
    produtos = Produto.objects.all().values_list('nome', flat=True)
    listadeprodutos = list(produtos)

    return JsonResponse(listadeprodutos, safe=False)


def procurarproduto(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            produto = Produto.objects.filter(
                nome__contains=searchedterm).first()

            if produto:
                return redirect('categorias/'+produto.Categoria.slug+'/'+produto.slug)
            else:
                messages.info(
                    request, "Nenhum produto encontrado com esta pesquisa")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
