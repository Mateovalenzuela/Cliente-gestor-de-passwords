from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from db_postgresql import Conexion
from apps.gestor.models.ModelPassword import ModelPassword
from apps.gestor.models.entities.Password import Password

objeto_conexion = Conexion.obtener_conexion()


# Create your views here.
@login_required
def home(request):
    passwords = ModelPassword.obtener_todos(objeto_conexion)
    messages.success(request, '¡Contraseñas listadas!')
    return render(request, "gestionPasswords.html", {"passwords": passwords})


@login_required
def registrar_password(request):
    usuario = request.POST['txt-registrar-usuario']
    password = request.POST['txt-registrar-password']
    url = request.POST['txt-registrar-url']
    nombreSitio = request.POST['txt-registrar-nombre_sitio']
    descripcion = request.POST['txt-registrar-descripcion']

    objPassword = Password(None, usuario, password, url, nombreSitio, descripcion)

    ModelPassword.insertar_password(objeto_conexion, objPassword)
    messages.success(request, '¡Contraseña registrada!')
    return redirect('/')


@login_required
def editar_password(request, id):
    usuario = request.POST[f'txt-editar-usuario-{id}']
    password = request.POST[f'txt-editar-password-{id}']
    url = request.POST[f'txt-editar-url-{id}']
    nombreSitio = request.POST[f'txt-editar-nombre_sitio-{id}']
    descripcion = request.POST[f'txt-editar-descripcion-{id}']

    objPassword = Password(id, usuario, password, url, nombreSitio, descripcion)
    ModelPassword.actualizar(objeto_conexion, objPassword)

    messages.success(request, '¡Contraseña actualizada!')
    return redirect('/')


@login_required
def eliminar_password(request, id):
    ModelPassword.eliminar(objeto_conexion, id)
    messages.success(request, '¡Contraseña eliminada!')
    return redirect('/')
