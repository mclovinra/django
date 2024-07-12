from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

# Validador personalizado para asegurar que el campo solo contenga números
def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError('Este campo solo acepta números.')

# Manager personalizado para el modelo Cliente
class ClienteManager(BaseUserManager):
    # Método para crear un usuario estándar
    def create_user(self, rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password=None, **extra_fields):
        if not rut_cli:
            raise ValueError('El Rut debe ser establecido')
        rut_cli = self.normalize_email(rut_cli)  # Normalizar el rut_cli, aunque debería ser self.normalize_username(rut_cli)
        user = self.model(
            rut_cli=rut_cli, dv_cli=dv_cli, nombre_cli=nombre_cli, ape_pat_cli=ape_pat_cli, ape_mat_cli=ape_mat_cli,
            fecha_nac_cli=fecha_nac_cli, telefono_cli=telefono_cli, mail_cli=mail_cli, dir_cli=dir_cli, **extra_fields
        )
        user.set_password(password)  # Establecer la contraseña usando el método set_password
        user.save(using=self._db)  # Guardar el usuario en la base de datos
        return user

    # Método para crear un superusuario
    def create_superuser(self, rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Establecer is_staff como True para un superusuario
        extra_fields.setdefault('is_superuser', True)  # Establecer is_superuser como True para un superusuario

        return self.create_user(rut_cli, dv_cli, nombre_cli, ape_pat_cli, ape_mat_cli, fecha_nac_cli, telefono_cli, mail_cli, dir_cli, password, **extra_fields)

# Modelo de Cliente personalizado que hereda de AbstractBaseUser
class Cliente(AbstractBaseUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente')  # Relación uno a uno con el modelo de usuario de Django
    rut_cli = models.CharField(primary_key=True, max_length=8, validators=[validate_only_numbers])  # Campo Rut como clave primaria
    dv_cli = models.CharField(max_length=1)  # Campo dígito verificador del Rut
    nombre_cli = models.CharField(max_length=20)  # Nombre del cliente
    ape_pat_cli = models.CharField(max_length=25)  # Apellido paterno del cliente
    ape_mat_cli = models.CharField(max_length=25)  # Apellido materno del cliente
    fecha_nac_cli = models.DateField()  # Fecha de nacimiento del cliente
    telefono_cli = models.CharField(max_length=15)  # Teléfono del cliente
    mail_cli = models.EmailField()  # Correo electrónico del cliente
    dir_cli = models.CharField(max_length=60)  # Dirección del cliente

    is_active = models.BooleanField(default=True)  # Indica si el cliente está activo
    is_staff = models.BooleanField(default=False)  # Indica si el cliente es personal administrativo

    objects = ClienteManager()  # Instancia del manager personalizado para este modelo

    USERNAME_FIELD = 'rut_cli'  # Campo que se utilizará para identificar al usuario al iniciar sesión
    REQUIRED_FIELDS = ['dv_cli', 'nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'telefono_cli', 'mail_cli', 'dir_cli']  # Campos requeridos al crear un usuario

    # Método para guardar el objeto en la base de datos
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # Método para obtener el nombre completo del cliente
    def get_full_name(self):
        return f'{self.nombre_cli} {self.ape_pat_cli} {self.ape_mat_cli}'

    # Método para obtener el nombre corto del cliente
    def get_short_name(self):
        return self.nombre_cli

    # Método para verificar si el cliente tiene una contraseña utilizable
    def has_usable_password(self):
        return True

    # Método para verificar la contraseña del cliente
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # Método para establecer la contraseña del cliente
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    # Método para obtener una representación de cadena del objeto Cliente
    def __str__(self):
        return f"{self.rut_cli} - {self.nombre_cli}"

    # Clase Meta que define metadatos del modelo
    class Meta:
        verbose_name = _('cliente')  # Nombre singular del modelo en la interfaz administrativa
        verbose_name_plural = _('clientes')  # Nombre plural del modelo en la interfaz administrativa

# Señal para eliminar el User cuando se elimina el Cliente
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Cliente)
def delete_user_on_cliente_delete(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except User.DoesNotExist:
        pass
