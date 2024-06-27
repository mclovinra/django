from django.db import models

class Producto(models.Model):
    id_prod = models.IntegerField(primary_key = True)
    titulo_prod = models.CharField(max_length = 50)
    volumen_prod = models.IntegerField()
    desc_prod = models.CharField(max_length = 200)
    precio_prod = models.IntegerField()
    stock_prod = models.IntegerField()
    editorial_prod = models.CharField(max_length = 30)

    def __str__(self):
        return self.titulo_prod


class Categoria(models.Model):
    id_cat =  models.IntegerField(primary_key = True)
    desc_cat = models.CharField(max_length = 25)

    def __str__(self):
        return self.desc_cat
        

class CategoriaProd(models.Model):
    id_catego = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_produc = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_catego', 'id_produc')

    def __str__(self):
        return f'{self.id_catego.desc_cat} - {self.id_produc.titulo_prod}'