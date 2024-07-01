from django.db import models
from django.core.exceptions import ValidationError

def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError('Este campo solo acepta números.')

class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=8, validators=[validate_only_numbers])
    dv_cli = models.CharField(max_length=1)
    nombre_cli = models.CharField(max_length=20)
    ape_pat_cli = models.CharField(max_length=25)
    ape_mat_cli = models.CharField(max_length=25)
    fecha_nac_cli = models.DateField()
    telefono_cli = models.CharField(max_length=15)
    mail_cli = models.EmailField()
    dir_clie = models.CharField(max_length=60)
    pass_cli = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.rut_cli} - {self.nombre_cli}"
