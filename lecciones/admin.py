from lecciones.models import  GrupoClase, Pregunta, ElegirRespuesta, PreguntaRespondida, Rol, Usuario
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


from .form import ELegirInlineFormset
#User = get_user_model()
# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):    
    model=ElegirRespuesta
    can_delete =False
    max_num= ElegirRespuesta.MAXIMO_RESPUESTA
    min_num= ElegirRespuesta.MAXIMO_RESPUESTA
    formset= ELegirInlineFormset 


class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines= (ElegirRespuestaInline, )
    list_display = ['leccion', 'texto']
    search_fields=['texto', 'leccion']
    

class PreguntasRespondidasAdmin(admin.ModelAdmin):   
    list_display = ['quizUser', 'pregunta', 'respuesta', 'correcta', 'puntaje_obtenido'] 
    search_fields=['quizUser__usuario__username']   
    class Meta:
        model= PreguntaRespondida

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'puntaje_total')
    list_filter = ('puntaje_total',)
    search_fields = ('puntaje_total',)


class ElegirRespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'texto')  




# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('GrupoClase', {'fields': ('grupoClase',)}),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('grupoClase',)}),
#    )


admin.site.register(PreguntaRespondida, PreguntasRespondidasAdmin)
admin.site.register(Pregunta, PreguntaAdmin);
admin.site.register(ElegirRespuesta, ElegirRespuestaAdmin);
admin.site.register(Usuario, UsuarioAdmin);
admin.site.register(GrupoClase);
admin.site.register(Rol);
# admin.site.register(User, CustomUserAdmin)