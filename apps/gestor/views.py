from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from db_postgresql import Conexion
from apps.gestor.models.entities.Password import Password
from apps.gestor import services

objeto_conexion = Conexion.obtener_conexion()


# Create your views here.
@login_required
def home(request):
    passwords = services.get_passwords()
    listaDePasswords = []
    for password in passwords:
        objPassword = Password(
            password['id'], password['usuario'], password['password'], password['url'], password['titulo'],
            password['descripcion']
        )
        listaDePasswords.append(objPassword)

    messages.success(request, '¡Contraseñas listadas!')
    return render(request, "gestionPasswords.html", {"passwords": listaDePasswords})


@login_required
def registrar_password(request):
    usuario = request.POST['txt-registrar-usuario']
    password = request.POST['txt-registrar-password']
    url = request.POST['txt-registrar-url']
    titulo = request.POST['txt-registrar-nombre_sitio']
    descripcion = request.POST['txt-registrar-descripcion']

    objPassword = Password(None, usuario, password, url, titulo, descripcion)

    services.add_password(objPassword.to_json())
    messages.success(request, '¡Contraseña registrada!')
    return redirect('/')


@login_required
def editar_password(request, id):
    usuario = request.POST[f'txt-editar-usuario-{id}']
    password = request.POST[f'txt-editar-password-{id}']
    url = request.POST[f'txt-editar-url-{id}']
    titulo = request.POST[f'txt-editar-nombre_sitio-{id}']
    descripcion = request.POST[f'txt-editar-descripcion-{id}']

    objPassword = Password(id, usuario, password, url, titulo, descripcion)
    services.update_password(objPassword.to_json())

    messages.success(request, '¡Contraseña actualizada!')
    return redirect('/')


@login_required
def eliminar_password(request, id):
    services.delete_password(id)
    messages.success(request, '¡Contraseña eliminada!')
    return redirect('/')
