from django import forms
from .models import Cliente

# Formulario de registro para clientes
class ClienteRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")  # Campo de contraseña
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")  # Campo para confirmar contraseña

    class Meta:
        model = Cliente  # Modelo al que pertenece el formulario
        fields = ['rut_cli', 'dv_cli', 'nombre_cli', 'ape_pat_cli', 'ape_mat_cli', 'fecha_nac_cli', 'telefono_cli', 'mail_cli', 'dir_cli']  # Campos que incluirá el formulario
        widgets = {
            'fecha_nac_cli': forms.DateInput(attrs={'type': 'date'})  # Widget para el campo de fecha de nacimiento
        }

    # Método para validar que las contraseñas coincidan
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")  # Error si las contraseñas no coinciden
        return cleaned_data

    # Método para guardar el formulario y crear el usuario
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Encriptar la contraseña
        if commit:
            user.save()
        return user


# Formulario de inicio de sesión para clientes
class ClienteLoginForm(forms.Form):
    rut = forms.CharField(max_length=20, required=True, label='Rut')  # Campo para el Rut del cliente
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Contraseña')  # Campo para la contraseña del cliente
