from lecciones.models import  Pregunta, ElegirRespuesta, PreguntaRespondida, Rol, Usuario
from django.contrib import admin

# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
    model=ElegirRespuesta
    max_num= ElegirRespuesta.MAXIMO_RESPUESTA
    min_num= ElegirRespuesta.MAXIMO_RESPUESTA


class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines= (ElegirRespuestaInline, )
    list_display = ['texto',]
    search_fields=['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display =['pregunta', 'respuesta', 'correcta']

    class Meta:
        model= PreguntaRespondida

admin.site.register(Usuario);

admin.site.register(Pregunta, PreguntaAdmin);


admin.site.register(ElegirRespuesta);
admin.site.register(Rol);