from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError('Este campo solo acepta números.')

class ClienteManager(BaseUserManager):
    def create_user(self, rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password=None, **extra_fields):
        if not rut_cli:
            raise ValueError('El Rut debe ser establecido')
        rut_cli = self.normalize_email(rut_cli)
        user = self.model(
            rut_cli=rut_cli, dv_cli=dv_cli, nombre_cli=nombre_cli, ape_pat_cli=ape_pat_cli, ape_mat_cli=ape_mat_cli,
            fecha_nac_cli=fecha_nac_cli, telefono_cli=telefono_cli, mail_cli=mail_cli, dir_cli=dir_cli, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password, **extra_fields)

class Cliente(AbstractBaseUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rut_cli = models.CharField(primary_key=True, max_length=8, validators=[validate_only_numbers])
    dv_cli = models.CharField(max_length=1)
    nombre_cli = models.CharField(max_length=20)
    ape_pat_cli = models.CharField(max_length=25)
    ape_mat_cli = models.CharField(max_length=25)
    fecha_nac_cli = models.DateField()
    telefono_cli = models.CharField(max_length=15)
    mail_cli = models.EmailField()
    dir_cli = models.CharField(max_length=60)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'rut_cli'
    REQUIRED_FIELDS = ['dv_cli', 'nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'telefono_cli', 'mail_cli', 'dir_cli']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f'{self.nombre_cli} {self.ape_pat_cli} {self.ape_mat_cli}'

    def get_short_name(self):
        return self.nombre_cli

    def has_usable_password(self):
        return True

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"{self.rut_cli} - {self.nombre_cli}"

    class Meta:
        verbose_name = _('cliente')
        verbose_name_plural = _('clientes')
