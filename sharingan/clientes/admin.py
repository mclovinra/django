from django.contrib import admin
from .models import Cliente

# Registro del modelo Cliente en el panel de administración de Django
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Lista de campos a mostrar en la vista de lista del panel de administración
    list_display = ['rut_cli', 'dv_cli', 'nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'telefono_cli', 'mail_cli', 'dir_cli']
    
    # Filtros para facilitar la búsqueda y filtrado en el panel de administración
    list_filter = ['nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'mail_cli']
    
    # Campos editables directamente desde la vista de lista en el panel de administración
    list_editable = ['nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'telefono_cli', 'mail_cli', 'dir_cli']
