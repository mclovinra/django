from django.shortcuts import render, redirect
from .forms import ClienteRegisterForm, ClienteLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from clientes.auth_backends import ClienteBackend
from django.contrib import messages
from clientes.models import Cliente


def validar_rut(rut, dv ):

    dv_ingresado = dv.upper()
    
    # Validar que el número sea válido
    try:
        int_rut = int(rut)
    except ValueError:
        return False, "RUT no es numérico"
    
    # Validar dígito verificador
    suma = 0
    multiplo = 2
    for reverso in reversed(rut):
        suma += int(reverso) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2
    
    dv_calculado = 11 - suma % 11
    
    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    
    dv_calculado = str(dv_calculado)
    
    if dv_calculado == dv_ingresado:
        print(f'{dv_ingresado} - {dv_calculado}')
        return True, "RUT válido"
    else:
        return False, "RUT inválido"

def registro_view(request):
    if request.method == 'POST':

        form = ClienteRegisterForm(request.POST)

        rut_cli = request.POST.get('rut_cli')
        dv_cli = request.POST.get('dv_cli')

        #Funcion que valida si el RUT es valido en conjunto al digito verificador
        es_valido, mensaje = validar_rut(rut_cli, dv_cli)
        if not es_valido:
            messages.error(request, 'El RUT no es válido')
            return render(request, 'registro.html', {'form': form})

        #Verifica el rut para mostrar un mensaje y no permitir el registro
        if Cliente.objects.filter(rut_cli=rut_cli).exists():
            messages.error(request, 'El RUT ingresado ya existe')

        else:
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

                return redirect('login')  # Redirige al usuario a la página de inicio de sesión

            else:
                pass1=form.cleaned_data['password1']
                pass2=form.cleaned_data['password2']

                if pass1 != pass2:
                    messages.error(request, 'Las contraseñas no coinciden')

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