from django.forms.models import modelform_factory
from lecciones.models import Pregunta, Respuesta, Usuario
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



@login_required(login_url="/login/")
def curso(request):
    return render(request, "dashboard.html")

@login_required(login_url="/login/")
def leccion1(request):
    return render(request, "./lecciones/leccion1.html")

@login_required(login_url="/login/")
def leccion1_1(request):
    return render(request, "./lecciones/leccion1.1.html")


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


@login_required(login_url="/login/")
def leccion3(request):
    return render(request, "./lecciones/leccion3.html")

@login_required(login_url="/login/")
def leccion4(request):
    return render(request, "./lecciones/leccion4.html")

@login_required(login_url="/login/")
def leccion5(request):
    return render(request, "./lecciones/leccion5.html")

@login_required(login_url="/login/")
def leccion6(request):
    return render(request, "./lecciones/leccion6.html")

@login_required(login_url="/login/")
def leccion7(request):
    return render(request, "./lecciones/leccion7.html")