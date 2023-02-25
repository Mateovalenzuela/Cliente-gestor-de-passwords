from django.urls import path
from apps.gestor import views

# Create your views here.

app_name = 'gestor'

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarPassword/', views.registrar_password),
    path('editarPassword/<id>', views.editar_password),
    path('eliminarPassword/<id>', views.eliminar_password),
]