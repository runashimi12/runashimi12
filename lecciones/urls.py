from lecciones.views import *
from django.urls import path, re_path
from app import views

urlpatterns = [
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


    path("leccion1/", leccion1, name="leccion1"),
    path("leccion1.1/", leccion1_1, name="leccion1_1"),
    path("leccion1.2/", leccion1_2, name="leccion1_2"),
    path("leccion1.3/", leccion1_3, name="leccion1_3"),

    
    path("leccion2/", leccion2, name="leccion2"),
    path("leccion2.1/", leccion2_1, name="leccion2_1"),
    path("leccion2.2/", leccion2_2, name="leccion2_2"),
    path("leccion2.3/", leccion2_3, name="leccion2_3"),
    path("leccion3/", leccion3, name="leccion3"),
    path("leccion4/", leccion4, name="leccion4"),
    path("leccion5/", leccion5, name="leccion5"),
    path("leccion6/", leccion6, name="leccion6"),
    path("leccion7/", leccion7, name="leccion7"),
]