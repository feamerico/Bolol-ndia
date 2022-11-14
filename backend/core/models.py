from django.db import models

from django.contrib.auth.models import User


class TipoItem(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return str(self.title)


class ItemPadr(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)  # type: ignore
    tipo = models.ForeignKey(
        TipoItem, related_name='itens', on_delete=models.CASCADE, null=True)  # type: ignore

    def __str__(self):
        return str(self.title)


class Pedido(models.Model):
    created_by = models.ForeignKey(
        User, related_name='pedidos', on_delete=models.CASCADE)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    # type: ignore
    cancelled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)  # type: ignore


class ItensPedidos(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemPadr, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('pedido', 'item')
