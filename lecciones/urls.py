from lecciones.views import *
from django.urls import path, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    #admins 
    path('admin/', admin.site.urls),
    path("curso/", curso, name="curso" ),
    # respuesta
    path("list_rta/", list_rta, name="list_rta" ),
    path("agregar_rta/", agregarRespuesta, name="agregar_rta" ),
    path("detalle_rta/<int:id>", detalleRespuesta, name="detalle_rta" ),
    path("editar_rta/<int:id>", editarRespuesta, name="editar_rta" ),
    path("eliminar_rta/<int:id>", eliminarRespuesta, name="eliminar_rta" ),

    # pregunta
    path("list_pregunta/", listPregunta, name="list_pregunta" ),
    path("agregar_pregunta/", agregarPregunta, name="agregar_pregunta" ),
    path("detalle_pregunta/<int:id>", detallePregunta, name="detalle_pregunta" ),
    path("editar_pregunta/<int:id>", editarPregunta, name="editar_pregunta" ),
    path("eliminar_pregunta/<int:id>", eliminarPregunta, name="eliminar_pregunta" ),

    #usuarios
    path("list_usuario/", listUsuario, name="list_usuario" ),
    path("agregar_usuario/", agregarUsuario, name="agregar_usuario" ),
    path("detalle_usuario/<int:id>", detalleUsuario, name="detalle_usuario" ),
    path("editar_usuario/<int:id>", editarUsuario, name="editar_usuario" ),
    path("eliminar_usuario/<int:id>", eliminarUsuario, name="eliminar_usuario" ),


    #roles
    path("list_roles/", listRoles, name="list_roles" ),
    path("agregar_roles/", agregarRoles, name="agregar_roles" ),
    path("detalle_roles/<int:id>", detalleRoles, name="detalle_roles" ),
    path("editar_roles/<int:id>", editarRoles, name="editar_roles" ),
    path("eliminar_roles/<int:id>", eliminarRoles, name="eliminar_roles" ),


    #tablero
    path('tablero/', tablero, name='tablero'),
    #path('resultado/(?P<int:pregunta_respondida_pk>\d+)/(?P<puntaje_total>\d+)', resultado_pregunta, name='resultado'),
    path('resultado/(<int:pregunta_respondida_pk>\d+)/(<puntaje_total>\d+)', resultado_pregunta, name='resultado'),


    path("leccion1/", leccion1, name="leccion1"),
    path("leccion1.1/", leccion1_1, name="leccion1_1"),
    path("leccion1.2/", leccion1_2, name="leccion1_2"),
    path("leccion1.3/", leccion1_3, name="leccion1_3"),

    
    path("leccion2/", leccion2, name="leccion2"),
    path("leccion2.1/", leccion2_1, name="leccion2_1"),
    path("leccion2.2/", leccion2_2, name="leccion2_2"),
    path("leccion2.3/", leccion2_3, name="leccion2_3"),
    path("leccion3/", leccion3, name="leccion3"),
    path("leccion3.1/", leccion3_1, name="leccion3_1"),
    path("leccion3.2/", leccion3_2, name="leccion3_2"),
    path("leccion3.3/", leccion3_3, name="leccion3_3"),
    path("leccion4/", leccion4, name="leccion4"),
    path("leccion4.1/", leccion4_1, name="leccion4_1"),
    path("leccion4.2/", leccion4_2, name="leccion4_2"),
    path("leccion4.3/", leccion4_3, name="leccion4_3"),
    path("leccion5/", leccion5, name="leccion5"),
    path("leccion5.1/", leccion5_1, name="leccion5_1"),
    path("leccion5.2/", leccion5_2, name="leccion5_2"),
    path("leccion5.3/", leccion5_3, name="leccion5_3"),
    path("leccion5.4/", leccion5_4, name="leccion5_4"),
    path("leccion6/", leccion6, name="leccion6"),
    path("leccion6.1/", leccion6_1, name="leccion6_1"),
    path("leccion6.2/", leccion6_2, name="leccion6_2"),
    path("leccion6.3/", leccion6_3, name="leccion6_3"),
    path("leccion7/", leccion7, name="leccion7"),
    path("leccion7.1/", leccion7_1, name="leccion7_1"),
    path("leccion7.2/", leccion7_2, name="leccion7_2"),
    path("leccion7.3/", leccion7_3, name="leccion7_3"),
    path("leccion8/", leccion8, name="leccion8"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)