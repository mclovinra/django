from django.db import models
from clientes.models import Cliente
from tienda.models import Producto 

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key = True)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total_pedido = models.IntegerField()

    def __str__(self):
        return f'{self.id_pedido}'

class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad_producto = models.IntegerField()

    class Meta:
        unique_together = ('id_pedido', 'id_producto')

    def __str__(self):
        return f'{self.id_pedido} - {self.id_producto}'