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
                username=form.cleaned_data['rut_cli'],
                password=form.cleaned_data['password1']
            )
            user.save()

            # Luego crear el objeto Cliente y enlazarlo al User
            cliente = form.save(commit=False)
            cliente.user = user
            cliente.save()

            messages.success(request, 'Registro completado exitosamente.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = ClienteRegisterForm()

    return render(request, 'clientes/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            password = form.cleaned_data.get('password')

            user = ClienteBackend.authenticate(request, rut_cli=rut, password=password)
            
            if user is not None:
                login(request, user, backend='clientes.auth_backends.ClienteBackend')
                print(f"Usuario {rut} ha iniciado sesión correctamente.")
                return redirect('home')
            else:
                print(f"Intento de inicio de sesión fallido para usuario {rut}.")
                form.add_error(None, 'Rut o contraseña incorrectos')
    else:
        form = ClienteLoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')