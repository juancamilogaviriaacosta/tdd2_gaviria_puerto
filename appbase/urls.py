from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^editar/(?P<idTrabajador>\d+)$', views.editar_perfil, name='editar'),
    url(r'^login$', views.login),
    url(r'^register', views.register),
    url(r'^logout$', views.logout),
    url(r'^trabajador/(?P<pk>\d+)$', views.detalle_trabajador, name='trabajador'),
    url(r'^mostrarTrabajadores/(?P<tipo>\w+)$', views.mostrarTrabajadores),
    url(r'^mostrarTrabajadores', views.mostrarTrabajadores),
    url(r'^tipoServicio/(?P<pk>\d+)$', views.getTiposDeServicio),
]