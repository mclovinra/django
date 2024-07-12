from django.db import models
from tienda.models import Producto
from clientes.models import Cliente

class Carro(models.Model):
    id_pedido = models.AutoField(primary_key=True)  # Identificador único para cada pedido
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con el modelo Cliente
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total del pedido

    def __str__(self):
        # Representación en cadena del objeto Carro
        return f"Carro de {self.cliente.nombre_cli} {self.cliente.ape_pat_cli}"

    @classmethod
    def create_with_items(cls, cliente, items):
        # Método de clase para crear un carro con items iniciales
        carro = cls(cliente=cliente)  # Crea una instancia del carro con el cliente especificado
        carro.save()  # Guarda la instancia del carro en la base de datos

        for item_data in items:  # Itera sobre los datos de los items
            producto = item_data['producto']  # Obtiene el producto del item
            quantity = item_data['quantity']  # Obtiene la cantidad del item
            CarroItem.objects.create(carro=carro, producto=producto, quantity=quantity)  # Crea y guarda el item en la base de datos

        return carro  # Retorna la instancia del carro

    def update_total(self):
        # Método para actualizar el total del pedido basado en los items del carro
        total = sum(item.quantity * item.producto.precio_prod for item in self.items.all())  # Calcula el total sumando el precio de cada item
        self.total_pedido = total  # Actualiza el total del pedido
        self.save()  # Guarda la instancia del carro en la base de datos


class CarroItem(models.Model):
    carro = models.ForeignKey(Carro, related_name='items', on_delete=models.CASCADE)  # Relación con el modelo Carro
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el modelo Producto
    quantity = models.PositiveIntegerField(default=1)  # Cantidad del producto en el carro

    def __str__(self):
        # Representación en cadena del objeto CarroItem
        return f"{self.quantity} de {self.producto.titulo_prod}"