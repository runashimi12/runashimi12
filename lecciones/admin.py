from lecciones.models import  Pregunta, Respuesta, Usuario
from django.contrib import admin

# Register your models here.

admin.site.register(Usuario);

admin.site.register(Pregunta);


admin.site.register(Respuesta);