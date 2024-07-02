from django.shortcuts import render, redirect
from .forms import ClienteRegisterForm, ClienteLoginForm
from django.contrib.auth import login, logout, authenticate
from clientes.auth_backends import ClienteBackend




def registro_view(request):
    if request.method == 'POST':
        form = ClienteRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteRegisterForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            password = form.cleaned_data.get('password')
            
            # Aquí especificamos el backend de autenticación
            user = authenticate(request, rut=rut, password=password, backend='clientes.auth_backends.ClienteBackend')
            
            if user is not None:
                login(request, user, backend='clientes.auth_backends.ClienteBackend')  # Especificamos el backend nuevamente
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