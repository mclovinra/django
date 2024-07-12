from django.db import models
from tienda.models import Producto
from clientes.models import Cliente
from django.core.exceptions import ObjectDoesNotExist

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar el pedido
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cliente asociado al pedido
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total del pedido

    def __str__(self):
        return f"Pedido #{self.id_pedido} - Cliente: {self.cliente.nombre_cli} {self.cliente.ape_pat_cli}"
        # Representación en cadena del pedido, mostrando su número y el nombre completo del cliente

    @classmethod
    def crear_desde_carro(cls, carro):
        # Método de clase para crear un pedido a partir de un carro
        pedido = cls(cliente=carro.cliente)  # Crear una instancia de Pedido con el cliente del carro
        pedido.save()  # Guardar el pedido en la base de datos

        try:
            for carro_item in carro.items.all():  # Iterar sobre todos los ítems del carro
                producto = carro_item.producto  # Obtener el producto del carro_item
                cantidad = carro_item.quantity  # Obtener la cantidad del carro_item

                # Crear un detalle de pedido asociado al pedido actual
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio_prod  # Precio unitario del producto en el momento del pedido
                )

                # Actualizar el stock del producto restando la cantidad pedida
                producto.stock_prod -= cantidad
                producto.save()

            pedido.actualizar_total()  # Calcular y actualizar el total del pedido

        except ObjectDoesNotExist:
            return None

        carro.delete()  # Eliminar el carro y sus ítems después de crear el pedido

        return pedido  # Devolver el pedido creado

    def actualizar_total(self):
        # Método para calcular y actualizar el total del pedido basado en los detalles del pedido
        total = sum(detalle.cantidad * detalle.precio_unitario for detalle in self.detallepedido_set.all())
        # Calcular el total sumando el precio unitario de cada detalle multiplicado por la cantidad
        self.total_pedido = total  # Actualizar el total del pedido
        self.save()  # Guardar los cambios en la base de datos

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Pedido al que pertenece este detalle
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto incluido en este detalle
    cantidad = models.PositiveIntegerField(default=1)  # Cantidad del producto incluido en el detalle
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio unitario del producto

    def __str__(self):
        return f"Detalle del pedido #{self.pedido.id_pedido} - Producto: {self.producto.titulo_prod}"
        # Representación en cadena del detalle del pedido, mostrando el número de pedido y el título del producto
