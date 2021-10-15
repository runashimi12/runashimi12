from django.forms.models import modelform_factory
from lecciones.models import Pregunta, Respuesta, Rol, Usuario
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.
from django.contrib.auth.decorators import login_required

# respuesta

@login_required(login_url="/login/")
def list_rta(request):
    no_respuesta=Respuesta.objects.count()
    respuestas= Respuesta.objects.all() #hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    return render(request, "./respuestas/list.html",{'no_respuesta':no_respuesta, 'respuestas': respuestas} )

def detalleRespuesta(request, id):
	# persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
	respuesta= get_object_or_404(Respuesta, pk=id)
	return render(request, './respuestas/detalle.html',{'respuesta':respuesta})

RespuestaForm = modelform_factory(Respuesta, exclude=[]) #la clase de modelo que vamos a utilizar
def agregarRespuesta(request):
    if request.method == 'POST':
        formaPersona=RespuestaForm(request.POST) # request.POST vamos a obtener todos los parametros 
        if formaPersona.is_valid(): # si es valido podfemos guardar
            formaPersona.save()
            return redirect('list_rta') #direccion ahacia el inicio
    else:
        formaRespuesta= RespuestaForm()
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './respuestas/agregar.html', {'formaRespuesta':formaRespuesta })

RespuestaForm = modelform_factory(Respuesta, exclude=[]) #la clase de modelo que vamos a utilizar
def editarRespuesta(request, id):
    respuesta=get_object_or_404(Respuesta, pk=id)
    if request.method == 'POST':
        formaPersona=RespuestaForm(request.POST, instance=respuesta) # request.POST vamos a obtener todos los parametros 
        if formaPersona.is_valid(): # si es valido podfemos guardar
            formaPersona.save()
            return redirect('list_rta') #direccion ahacia el inicio
    else:
        formaRespuesta= RespuestaForm(instance=respuesta)
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './respuestas/editar.html', {'formaRespuesta':formaRespuesta })

def eliminarRespuesta(request, id):
	respuesta= get_object_or_404(Respuesta, pk=id)
#si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
	if respuesta:
		respuesta.delete()
	return redirect('list_rta') #direccion ahacia el inicio


# pregunta

@login_required(login_url="/login/")
def listPregunta(request):
    no_pregunta=Pregunta.objects.count()
    preguntas= Pregunta.objects.all() #hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    return render(request, "./pregunta/list.html",{'no_pregunta':no_pregunta, 'preguntas': preguntas} )


PreguntaForm = modelform_factory(Pregunta, exclude=[]) #la clase de modelo que vamos a utilizar
def agregarPregunta(request):
    if request.method == 'POST':
        formaPregunta=PreguntaForm(request.POST) # request.POST vamos a obtener todos los parametros 
        if formaPregunta.is_valid(): # si es valido podfemos guardar
            formaPregunta.save()
            return redirect('list_pregunta') #direccion ahacia el inicio
    else:
        formaPregunta= PreguntaForm()
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './pregunta/agregar.html', {'formaPregunta':formaPregunta })

def detallePregunta(request, id):
	# persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
	pregunta= get_object_or_404(Pregunta, pk=id)
	return render(request, './pregunta/detalle.html',{'pregunta':pregunta})


PreguntaForm = modelform_factory(Pregunta, exclude=[]) #la clase de modelo que vamos a utilizar
def editarPregunta(request, id):
    pregunta=get_object_or_404(Pregunta, pk=id)
    if request.method == 'POST':
        formaPregunta=PreguntaForm(request.POST, instance=pregunta) # request.POST vamos a obtener todos los parametros 
        if formaPregunta.is_valid(): # si es valido podfemos guardar
            formaPregunta.save()
            return redirect('list_pregunta') #direccion ahacia el inicio
    else:
        formaPregunta= PreguntaForm(instance=pregunta)
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './pregunta/editar.html', {'formaPregunta':formaPregunta })

def eliminarPregunta(request, id):
	pregunta= get_object_or_404(Pregunta, pk=id)
#si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
	if pregunta:
		pregunta.delete()
	return redirect('list_pregunta') #direccion ahacia el inicio

# usuarios

@login_required(login_url="/login/")
def listUsuario(request):
    no_usuario=Usuario.objects.count()
    usuarios= Usuario.objects.all() #hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    return render(request, "./usuarios/list.html",{'no_usuario':no_usuario, 'usuarios': usuarios} )


UsuarioForm = modelform_factory(Usuario, exclude=[]) #la clase de modelo que vamos a utilizar
def agregarUsuario(request):
    if request.method == 'POST':
        formaUsuario=UsuarioForm(request.POST) # request.POST vamos a obtener todos los parametros 
        if formaUsuario.is_valid(): # si es valido podfemos guardar
            formaUsuario.save()
            return redirect('list_usuario') #direccion ahacia el inicio
    else:
        formaUsuario= UsuarioForm()
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './usuarios/agregar.html', {'formaUsuario':formaUsuario })

def detalleUsuario(request, id):
	# persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
	usuario= get_object_or_404(Usuario, pk=id)
	return render(request, './usuarios/detalle.html',{'usuario':usuario})


UsuarioForm = modelform_factory(Usuario, exclude=[]) #la clase de modelo que vamos a utilizar
def editarUsuario(request, id):
    usuario=get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        formaUsuario=UsuarioForm(request.POST, instance=usuario) # request.POST vamos a obtener todos los parametros 
        if formaUsuario.is_valid(): # si es valido podfemos guardar
            formaUsuario.save()
            return redirect('list_usuario') #direccion ahacia el inicio
    else:
        formaUsuario= UsuarioForm(instance=usuario)
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './usuarios/editar.html', {'formaUsuario':formaUsuario })

def eliminarUsuario(request, id):
	usuario= get_object_or_404(Usuario, pk=id)
#si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
	if usuario:
		usuario.delete()
	return redirect('list_usuario') #direccion ahacia el inicio

 #Roles

@login_required(login_url="/login/")
def listRoles(request):
    no_roles=Rol.objects.count()
    roles= Rol.objects.all() #hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    return render(request, "./roles/list.html",{'no_roles': no_roles, 'roles': roles} )


RolesForm = modelform_factory(Rol, exclude=[]) #la clase de modelo que vamos a utilizar
def agregarRoles(request):
    if request.method == 'POST':
        formaRoles=RolesForm(request.POST) # request.POST vamos a obtener todos los parametros 
        if formaRoles.is_valid(): # si es valido podfemos guardar
            formaRoles.save()
            return redirect('list_roles') #direccion ahacia el inicio
    else:
        formaRoles= RolesForm()
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './roles/agregar.html', {'formaRoles':formaRoles })

def detalleRoles(request, id):
	# persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
	rol= get_object_or_404(Rol, pk=id)
	return render(request, './roles/detalle.html',{'rol':rol})


RolesForm = modelform_factory(Rol, exclude=[]) #la clase de modelo que vamos a utilizar
def editarRoles(request, id):
    rol=get_object_or_404(Rol, pk=id)
    if request.method == 'POST':
        formaRoles=RolesForm(request.POST, instance=rol) # request.POST vamos a obtener todos los parametros 
        if formaRoles.is_valid(): # si es valido podfemos guardar
            formaRoles.save()
            return redirect('list_roles') #direccion ahacia el inicio
    else:
        formaRoles= RolesForm(instance=rol)
	## mostrar el formulario 	primera vez que se va a mandar el metodo	
    return  render (request, './roles/editar.html', {'formaRoles':formaRoles })

def eliminarRoles(request, id):
	rol= get_object_or_404(Rol, pk=id)
#si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
	if rol:
		rol.delete()
	return redirect('list_roles') #direccion ahacia el inicio

@login_required(login_url="/login/")
def curso(request):
    return render(request, "dashboard.html")

@login_required(login_url="/login/")
def leccion1(request):
    return render(request, "./lecciones/leccion1.html")

@login_required(login_url="/login/")
def leccion1_1(request):
    if request.method == 'POST':
        formaPersona=RespuestaForm(request.POST) # request.POST vamos a obtener todos los parametros 
        if formaPersona.is_valid(): # si es valido podfemos guardar
            formaPersona.save()
            return redirect('list_rta') #direccion ahacia el inicio
    else:
        formaRespuesta= RespuestaForm()
    return render(request, "./lecciones/leccion1.1.html", {'formaRespuesta':formaRespuesta })



@login_required(login_url="/login/")
def leccion1_2(request):
    return render(request, "./lecciones/leccion1.2.html")

@login_required(login_url="/login/")
def leccion1_3(request):
    return render(request, "./lecciones/leccion1.3.html")


@login_required(login_url="/login/")
def leccion2(request):
    return render(request, "./lecciones/leccion2.html")

@login_required(login_url="/login/")
def leccion2_1(request):
    return render(request, "./lecciones/leccion2.1.html")

@login_required(login_url="/login/")
def leccion2_2(request):
    return render(request, "./lecciones/leccion2.2.html")

@login_required(login_url="/login/")
def leccion2_3(request):
    return render(request, "./lecciones/leccion2.3.html")

# INICIO leccion 3
@login_required(login_url="/login/")
def leccion3(request):
    return render(request, "./lecciones/leccion3.html")

@login_required(login_url="/login/")
def leccion3_1(request):
    return render(request, "./lecciones/leccion3.1.html")

@login_required(login_url="/login/")
def leccion3_2(request):
    return render(request, "./lecciones/leccion3.2.html")

@login_required(login_url="/login/")
def leccion3_3(request):
    return render(request, "./lecciones/leccion3.3.html")
# FIN leccion 3



# INICIO leccion 4
@login_required(login_url="/login/")
def leccion4(request):
    return render(request, "./lecciones/leccion4.html")

@login_required(login_url="/login/")
def leccion4_1(request):
    return render(request, "./lecciones/leccion4.1.html")

@login_required(login_url="/login/")
def leccion4_2(request):
    return render(request, "./lecciones/leccion4.2.html")

@login_required(login_url="/login/")
def leccion4_3(request):
    return render(request, "./lecciones/leccion4.3.html")
# FIN leccion 4



# INICIO leccion 5
@login_required(login_url="/login/")
def leccion5(request):
    return render(request, "./lecciones/leccion5.html")

@login_required(login_url="/login/")
def leccion5_1(request):
    return render(request, "./lecciones/leccion5.1.html")

@login_required(login_url="/login/")
def leccion5_2(request):
    return render(request, "./lecciones/leccion5.2.html")

@login_required(login_url="/login/")
def leccion5_3(request):
    return render(request, "./lecciones/leccion5.3.html")
# FIN leccion 5




# INICIO leccion 6
@login_required(login_url="/login/")
def leccion6(request):
    return render(request, "./lecciones/leccion6.html")

@login_required(login_url="/login/")
def leccion6_1(request):
    return render(request, "./lecciones/leccion6.1.html")

@login_required(login_url="/login/")
def leccion6_2(request):
    return render(request, "./lecciones/leccion6.2.html")

@login_required(login_url="/login/")
def leccion6_3(request):
    return render(request, "./lecciones/leccion6.3.html")
# FIN leccion 6



# INICIO leccion 7
@login_required(login_url="/login/")
def leccion7(request):
    return render(request, "./lecciones/leccion7.html")

@login_required(login_url="/login/")
def leccion7_1(request):
    return render(request, "./lecciones/leccion7.1.html")

@login_required(login_url="/login/")
def leccion7_2(request):
    return render(request, "./lecciones/leccion7.2.html")

@login_required(login_url="/login/")
def leccion7_3(request):
    return render(request, "./lecciones/leccion7.3.html")
# FIN leccion 7


