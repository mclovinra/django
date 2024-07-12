from django.db import models

class Producto(models.Model):
    id_prod = models.IntegerField(primary_key=True)  # Identificador único del producto
    titulo_prod = models.CharField(max_length=50)  # Título del producto
    volumen_prod = models.IntegerField()  # Volumen del producto
    desc_prod = models.CharField(max_length=200)  # Descripción del producto
    precio_prod = models.IntegerField()  # Precio del producto
    stock_prod = models.IntegerField()  # Cantidad en stock del producto
    editorial_prod = models.CharField(max_length=30)  # Editorial del producto
    tipo_prod = models.CharField(max_length=15, default='General')  # Tipo de producto
    img_prod = models.ImageField(upload_to="tienda", null=True)  # Imagen del producto

    def __str__(self):
        return f"{self.id_prod} - {self.titulo_prod}"  # Representación en cadena del producto

class Categoria(models.Model):
    id_cat = models.IntegerField(primary_key=True)  # Identificador único de la categoría
    desc_cat = models.CharField(max_length=25)  # Descripción de la categoría

    def __str__(self):
        return self.desc_cat  # Representación en cadena de la categoría

class CategoriaProd(models.Model):
    id_catego = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con la categoría
    id_produc = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el producto

    class Meta:
        unique_together = ('id_catego', 'id_produc')  # Restricción para asegurar unicidad

    def __str__(self):
        return f'{self.id_catego.desc_cat} - {self.id_produc.titulo_prod}'  # Representación en cadena de la relación entre categoría y producto