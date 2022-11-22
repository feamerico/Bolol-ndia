from django.db import models

import datetime
import os

from django.contrib.auth.models import User


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (original_filename, nowTime)
    return os.path.join('uploads/', filename)


class Categoria(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slug)


class Produto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    produto_imagem = models.ImageField(
        upload_to=get_file_path, null=True, blank=True)
    quantidade = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)
    valorcompra = models.FloatField(null=False, blank=False)
    valorvenda = models.FloatField(null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)  # type: ignore


class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    produto_qtd = models.IntegerField(null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)  # type: ignore


class Loja(models.Model):
    endereco = models.CharField(max_length=150, null=False, blank=False)
    cidade = models.CharField(max_length=150, null=False, blank=False)
    estado = models.CharField(max_length=150, null=False, blank=False)
    fechado = models.BooleanField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.endereco)


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, null=False, blank=False)
    sobrenome = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    telefone = models.CharField(max_length=150, null=False, blank=False)
    total_price = models.FloatField(null=False)
    forma_pagamento = models.CharField(max_length=150, null=False, blank=False)
    statuspedido = (
        ('Pendente', 'Pendente'),
        ('Em entrega', 'Em entrega'),
        ('Concluído', 'Concluído'),
    )
    status = models.CharField(
        max_length=150, choices=statuspedido, default='Pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.id)  # type: ignore


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.FloatField(null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return '{}'.format(self.pedido.id)  # type: ignore


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=50, null=False)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
