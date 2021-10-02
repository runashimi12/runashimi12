from lecciones.models import  Pregunta, Respuesta, Rol, Usuario
from django.contrib import admin

# Register your models here.

admin.site.register(Usuario);

admin.site.register(Pregunta);


admin.site.register(Respuesta);
admin.site.register(Rol);