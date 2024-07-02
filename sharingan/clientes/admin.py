from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut_cli','dv_cli'
                    ,'nombre_cli','ape_pat_cli'
                    ,'ape_mat_cli','fecha_nac_cli'
                    ,'telefono_cli','mail_cli'
                    ,'dir_cli','password']
    list_filter = ['nombre_cli','ape_pat_cli'
                    ,'ape_mat_cli','fecha_nac_cli'
                    ,'mail_cli']
    list_editable = ['nombre_cli','ape_pat_cli'
                    ,'ape_mat_cli','fecha_nac_cli'
                    ,'telefono_cli','mail_cli','dir_cli']
