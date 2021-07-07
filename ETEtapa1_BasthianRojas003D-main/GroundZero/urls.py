from django.urls import path
from . import views

urlpatterns=[
    path('Paginaprincipal/',views.Paginaprincipal, name='Paginaprincipal'),
    path('Productos/',views.Productos, name='Productos'),
    path('QuienesSomos/',views.QuienesSomos, name='QuienesSomos'),
    path('Registro/',views.Registro, name='Registro'),
    path('Despacho/',views.Despacho, name='Despacho'),
    path('Registros/',views.Registros, name='Registros'),
    path('crearRegistro/',views.crearRegistro, name='crearRegistro'),
    path('modRegistro/<id>',views.modRegistro, name='ModRegistro'),
    path('eliminar/<id>',views.eliminar, name='eliminar'),
]