from django.db import models
from tienda.models import Producto
from clientes.models import Cliente
from django.core.exceptions import ObjectDoesNotExist

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id_pedido} - Cliente: {self.cliente.nombre_cli} {self.cliente.ape_pat_cli}"

    @classmethod
    def crear_desde_carro(cls, carro):
        # Crear un pedido basado en el carro proporcionado
        pedido = cls(cliente=carro.cliente)
        pedido.save()

        try:
            # Transferir los ítems del carro al pedido y restar del stock
            for carro_item in carro.items.all():
                producto = carro_item.producto
                cantidad = carro_item.quantity

                # Crear el detalle del pedido
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio_prod
                )

                # Restar la cantidad del producto del stock
                producto.stock_prod -= cantidad
                producto.save()

            # Calcular el total del pedido y guardarlo
            pedido.actualizar_total()

        except ObjectDoesNotExist:
            return None

        # Eliminar el carro y sus ítems después de crear el pedido
        carro.delete()

        return pedido


    def actualizar_total(self):
        # Calcular el total del pedido basado en los detalles del pedido
        total = sum(detalle.cantidad * detalle.precio_unitario for detalle in self.detallepedido_set.all())
        self.total_pedido = total
        self.save()

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle del pedido #{self.pedido.id_pedido} - Producto: {self.producto.titulo_prod}"
