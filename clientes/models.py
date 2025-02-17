from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_pedido = models.DateField()
    valor_total = models.CharField(max_length=9)

    def __str__(self):
        return f'Pedido {self.id}'

class ItensPedido (models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco_unitario = models.CharField(max_length=9)

    def __str__(self):
        return self.produto