from django.contrib import admin
from .models import ItemPadr, Pedido, TipoItem, ItensPedidos


@admin.register(TipoItem)
class TipoItemModel(admin.ModelAdmin):
    model = TipoItem


@admin.register(ItemPadr)
class ItemPadrModel(admin.ModelAdmin):
    model = ItemPadr


@admin.register(Pedido)
class PedidoModel(admin.ModelAdmin):
    model = Pedido


@admin.register(ItensPedidos)
class ItensPedidosModel(admin.ModelAdmin):
    model = ItensPedidos
