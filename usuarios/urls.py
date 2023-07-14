from django.contrib import admin
from django.urls import path
from . import views

from mc.settings import STATIC_URL

urlpatterns = [
    path('', views.listEmpleados, name = 'listEmpleados'),
    path('new', views.nuevoEmpleado, name = 'nuevoEmpleado'),
    path('editar/<int:id>/', views.editarEmpleado, name = 'editarEmpleado'),
    path('eliminar/<int:id>/', views.eliminarEmpleado, name = 'eliminarEmpleado'),
    path('login', views.loginSession, name = 'login'),
    path('logout', views.logoutSession, name = 'logout'),
]