from django.contrib import admin
from appbase.models import TiposDeServicio
from appbase.models import Trabajador
from appbase.models import Comentario

admin.site.register(TiposDeServicio)
admin.site.register(Trabajador)
admin.site.register(Comentario)