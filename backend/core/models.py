from django.db import models

from django.contrib.auth.models import User


class Pedido(models.Model):
    itemnumber = models.IntegerField()
    totalprice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)  # type: ignore
    created_by = models.ForeignKey(
        User, related_name='pedidos', on_delete=models.CASCADE)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    cancelled_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.id


class ItemPadr(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)  # type: ignore
    inventory = models.IntegerField()
    pedidos = models.ForeignKey(
        Pedido, related_name='itens', on_delete=models.CASCADE)  # type: ignore
    preferencias = models.ForeignKey(
        User, related_name='itens', on_delete=models.CASCADE)  # type: ignore

    def __str__(self):
        return self.title
