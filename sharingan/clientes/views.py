from django.shortcuts import render, redirect
from .forms import ClienteRegisterForm, ClienteLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from clientes.auth_backends import ClienteBackend
from django.contrib import messages


def registro_view(request):
    if request.method == 'POST':
        form = ClienteRegisterForm(request.POST)
        if form.is_valid():
            # Crear el objeto User primero
            user = User.objects.create_user(
                username=form.cleaned_data['rut_cli'],  # Usa el rut_cli como nombre de usuario
                password=form.cleaned_data['password1']  # Obtiene la contraseña del formulario
            )
            user.save()  # Guarda el usuario en la base de datos

            # Luego crear el objeto Cliente y enlazarlo al User
            cliente = form.save(commit=False)  # Guarda el formulario ClienteRegisterForm
            cliente.user = user  # Asigna el usuario recién creado al cliente
            cliente.save()  # Guarda el cliente en la base de datos

            messages.success(request, 'Registro completado exitosamente.')  # Mensaje de éxito
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')  # Mensaje de error si el formulario no es válido
    else:
        form = ClienteRegisterForm()  # Crea un formulario vacío si el método no es POST

    return render(request, 'registro.html', {'form': form})  # Renderiza la plantilla 'registro.html' con el formulario


def login_view(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)  # Obtiene el formulario de inicio de sesión
        if form.is_valid():
            rut = form.cleaned_data.get('rut')  # Obtiene el rut del formulario
            password = form.cleaned_data.get('password')  # Obtiene la contraseña del formulario

            # Autenticación personalizada utilizando el backend ClienteBackend
            user = ClienteBackend.authenticate(request, rut_cli=rut, password=password)

            if user is not None:  # Si el usuario se autentica correctamente
                login(request, user, backend='clientes.auth_backends.ClienteBackend')  # Inicia sesión con el usuario
                print(f"Usuario {rut} ha iniciado sesión correctamente.")
                return redirect('home')  # Redirige al usuario a la página de inicio
            else:
                print(f"Intento de inicio de sesión fallido para usuario {rut}.")
                form.add_error(None, 'Rut o contraseña incorrectos')  # Agrega un error al formulario si la autenticación falla
    else:
        form = ClienteLoginForm()  # Crea un formulario vacío si el método no es POST

    return render(request, 'login.html', {'form': form})  # Renderiza la plantilla 'login.html' con el formulario


def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige al usuario a la página de inicio después de cerrar sesión