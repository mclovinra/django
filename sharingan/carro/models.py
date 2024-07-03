from django.db import models
from tienda.models import Producto
from clientes.models import Cliente

class Carro(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Carro de {self.cliente.nombre_cli} {self.cliente.ape_pat_cli}"

    @classmethod
    def create_with_items(cls, cliente, items):
        carro = cls(cliente=cliente)
        carro.save()

        for item_data in items:
            producto = item_data['producto']
            quantity = item_data['quantity']
            CarroItem.objects.create(carro=carro, producto=producto, quantity=quantity)

        return carro
    
    def update_total(self):
        # Calcular el total del pedido basado en los items del carro
        total = sum(item.quantity * item.producto.precio_prod for item in self.items.all())
        self.total_pedido = total
        self.save()

class CarroItem(models.Model):
    carro = models.ForeignKey(Carro, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} de {self.producto.titulo_prod}"
