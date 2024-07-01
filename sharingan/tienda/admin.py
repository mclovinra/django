from django.contrib import admin
from .models import Categoria, Producto, CategoriaProd

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_cat','desc_cat']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_prod','titulo_prod'
                    ,'volumen_prod','desc_prod'
                    ,'precio_prod','stock_prod'
                    ,'editorial_prod','tipo_prod']
    list_filter = ['id_prod','titulo_prod'
                    ,'desc_prod','editorial_prod']
    list_editable = ['precio_prod','stock_prod','tipo_prod']

@admin.register(CategoriaProd)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_catego','id_produc']
    list_filter = ['id_catego','id_produc']
