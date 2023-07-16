from django.contrib import admin
from django.urls import path
from . import views

from mc.settings import STATIC_URL

urlpatterns = [
    path('', views.listSchedules, name = 'listSchedules'),
    path('new', views.nuevoSchedule, name = 'nuevoSchedule'),
    path('editar/<int:id>/', views.editarSchedule, name = 'editarSchedule'),
    path('eliminar/<int:id>/', views.eliminarSchedule, name = 'eliminarSchedule'),
]