from datetime import datetime
from decimal import Decimal
import logging
import os
import time
from django.forms import DecimalField, IntegerField
from django.forms.models import modelform_factory
from django.http.response import Http404
from lecciones.models import Pregunta, ElegirRespuesta, PreguntaRespondida, Rol, Usuario
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Max, Value
from django.db.models.functions import Coalesce
from django.db.models import Sum


# Create your views here.
from django.contrib.auth.decorators import login_required

# respuesta


@login_required(login_url="/login/")
def list_rta(request):
    no_respuesta = ElegirRespuesta.objects.count()
    # hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    respuestas = ElegirRespuesta.objects.all()
    return render(request, "./respuestas/list.html", {'no_respuesta': no_respuesta, 'respuestas': respuestas})


def detalleRespuesta(request, id):
    # persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
    respuesta = get_object_or_404(ElegirRespuesta, pk=id)
    return render(request, './respuestas/detalle.html', {'respuesta': respuesta})


# la clase de modelo que vamos a utilizar
RespuestaForm = modelform_factory(ElegirRespuesta, exclude=[])


def agregarRespuesta(request):
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaPersona = RespuestaForm(request.POST)
        if formaPersona.is_valid():  # si es valido podfemos guardar
            formaPersona.save()
            return redirect('list_rta')  # direccion ahacia el inicio
    else:
        formaRespuesta = RespuestaForm()
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './respuestas/agregar.html', {'formaRespuesta': formaRespuesta})


# la clase de modelo que vamos a utilizar
RespuestaForm = modelform_factory(ElegirRespuesta, exclude=[])


def editarRespuesta(request, id):
    respuesta = get_object_or_404(ElegirRespuesta, pk=id)
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaPersona = RespuestaForm(request.POST, instance=respuesta)
        if formaPersona.is_valid():  # si es valido podfemos guardar
            formaPersona.save()
            return redirect('list_rta')  # direccion ahacia el inicio
    else:
        formaRespuesta = RespuestaForm(instance=respuesta)
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './respuestas/editar.html', {'formaRespuesta': formaRespuesta})


def eliminarRespuesta(request, id):
    respuesta = get_object_or_404(ElegirRespuesta, pk=id)
# si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
    if respuesta:
        respuesta.delete()
    return redirect('list_rta')  # direccion ahacia el inicio


# pregunta

@login_required(login_url="/login/")
def listPregunta(request):
    no_pregunta = Pregunta.objects.count()
    # hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    preguntas = Pregunta.objects.all()
    return render(request, "./pregunta/list.html", {'no_pregunta': no_pregunta, 'preguntas': preguntas})


# la clase de modelo que vamos a utilizar
PreguntaForm = modelform_factory(Pregunta, exclude=[])


def agregarPregunta(request):
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaPregunta = PreguntaForm(request.POST)
        if formaPregunta.is_valid():  # si es valido podfemos guardar
            formaPregunta.save()
            return redirect('list_pregunta')  # direccion ahacia el inicio
    else:
        formaPregunta = PreguntaForm()
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './pregunta/agregar.html', {'formaPregunta': formaPregunta})


def detallePregunta(request, id):
    # persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
    pregunta = get_object_or_404(Pregunta, pk=id)
    return render(request, './pregunta/detalle.html', {'pregunta': pregunta})


# la clase de modelo que vamos a utilizar
PreguntaForm = modelform_factory(Pregunta, exclude=[])


def editarPregunta(request, id):
    pregunta = get_object_or_404(Pregunta, pk=id)
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaPregunta = PreguntaForm(request.POST, instance=pregunta)
        if formaPregunta.is_valid():  # si es valido podfemos guardar
            formaPregunta.save()
            return redirect('list_pregunta')  # direccion ahacia el inicio
    else:
        formaPregunta = PreguntaForm(instance=pregunta)
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './pregunta/editar.html', {'formaPregunta': formaPregunta})


def eliminarPregunta(request, id):
    pregunta = get_object_or_404(Pregunta, pk=id)
# si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
    if pregunta:
        pregunta.delete()
    return redirect('list_pregunta')  # direccion ahacia el inicio

# usuarios


@login_required(login_url="/login/")
def listUsuario(request):
    no_usuario = Usuario.objects.count()
    # hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    usuarios = Usuario.objects.all()
    return render(request, "./usuarios/list.html", {'no_usuario': no_usuario, 'usuarios': usuarios})


# la clase de modelo que vamos a utilizar
UsuarioForm = modelform_factory(Usuario, exclude=[])


def agregarUsuario(request):
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaUsuario = UsuarioForm(request.POST)
        if formaUsuario.is_valid():  # si es valido podfemos guardar
            formaUsuario.save()
            return redirect('list_usuario')  # direccion ahacia el inicio
    else:
        formaUsuario = UsuarioForm()
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './usuarios/agregar.html', {'formaUsuario': formaUsuario})


def detalleUsuario(request, id):
    # persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
    usuario = get_object_or_404(Usuario, pk=id)
    return render(request, './usuarios/detalle.html', {'usuario': usuario})


# la clase de modelo que vamos a utilizar
UsuarioForm = modelform_factory(Usuario, exclude=[])


def editarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaUsuario = UsuarioForm(request.POST, instance=usuario)
        if formaUsuario.is_valid():  # si es valido podfemos guardar
            formaUsuario.save()
            return redirect('list_usuario')  # direccion ahacia el inicio
    else:
        formaUsuario = UsuarioForm(instance=usuario)
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './usuarios/editar.html', {'formaUsuario': formaUsuario})


def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
# si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
    if usuario:
        usuario.delete()
    return redirect('list_usuario')  # direccion ahacia el inicio

 # Roles


@login_required(login_url="/login/")
def listRoles(request):
    no_roles = Rol.objects.count()
    # hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    roles = Rol.objects.all()
    return render(request, "./roles/list.html", {'no_roles': no_roles, 'roles': roles})


# la clase de modelo que vamos a utilizar
RolesForm = modelform_factory(Rol, exclude=[])


def agregarRoles(request):
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaRoles = RolesForm(request.POST)
        if formaRoles.is_valid():  # si es valido podfemos guardar
            formaRoles.save()
            return redirect('list_roles')  # direccion ahacia el inicio
    else:
        formaRoles = RolesForm()
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './roles/agregar.html', {'formaRoles': formaRoles})


def detalleRoles(request, id):
    # persona = Persona.objects.get(pk=id) # en get ponemos el valor de una llave primaria para recuperar un objeto de tipo persona
    rol = get_object_or_404(Rol, pk=id)
    return render(request, './roles/detalle.html', {'rol': rol})


# la clase de modelo que vamos a utilizar
RolesForm = modelform_factory(Rol, exclude=[])


def editarRoles(request, id):
    rol = get_object_or_404(Rol, pk=id)
    if request.method == 'POST':
        # request.POST vamos a obtener todos los parametros
        formaRoles = RolesForm(request.POST, instance=rol)
        if formaRoles.is_valid():  # si es valido podfemos guardar
            formaRoles.save()
            return redirect('list_roles')  # direccion ahacia el inicio
    else:
        formaRoles = RolesForm(instance=rol)
        # mostrar el formulario 	primera vez que se va a mandar el metodo
    return render(request, './roles/editar.html', {'formaRoles': formaRoles})


def eliminarRoles(request, id):
    rol = get_object_or_404(Rol, pk=id)
# si se envio la informacion de tipo POST entonces ya tenemos que procesar nuestro formulario cad auno de los parametros qeu estamos enviando de nuestro cliente
    if rol:
        rol.delete()
    return redirect('list_roles')  # direccion ahacia el inicio


@login_required(login_url="/login/")
def curso(request):
    return render(request, "dashboard.html")


@login_required(login_url="/login/")
def leccion1(request):
    return render(request, "./lecciones/leccion1.html")


def tablero(request):
    logging.basicConfig(level=logging.NOTSET)  # He 
    max=0
    max_1=0
    max_2=0   
    total_usaurios_quiz = Usuario.objects.order_by('-puntaje_total')
    
    contador = total_usaurios_quiz.count()
    page = request.GET.get('page', 1)

    for i in range(0, len(total_usaurios_quiz)):
        if i==0:
            max= total_usaurios_quiz[0].puntaje_total
        elif i==1:
            max_1= total_usaurios_quiz[1].puntaje_total
        elif i==2:
            max_2= total_usaurios_quiz[2].puntaje_total
        else:
            max=0
            max_1=0
            max_2=0



    try:
        paginator= Paginator(total_usaurios_quiz, 10)
        total_usaurios_quiz = paginator.page(page)
    except:
        raise Http404

    context = {

        'entity': total_usaurios_quiz,
        'contar_user': contador,
        'paginator': paginator,
        'max':max,
        'max_1':max_1,
        'max_2':max_2
    }

    return render(request, './lecciones/tablero.html', context)


@login_required(login_url="/login/")
def leccion1_1(request):
    id = 1
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)
    contador=5
    hora=datetime.now().strftime("%H:%M:%S")    

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')  
        
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total = QuizUser.obtener_puntaje()        

        return redirect('resultado', pregunta_respondida.pk, puntaje_total)

    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)            

            context = {
                'pregunta': pregunta,
                'contador': contador,
                'hora': hora

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')


    return render(request, "./lecciones/leccion1.1.html", context)
 # if pregunta is not None:
  #          QuizUser.crear_intentos(pregunta)
    #    context = {
    #        'pregunta': pregunta

    #   }


def resultado_pregunta(request, pregunta_respondida_pk, puntaje_total):
    maximo_puntaje_total=0
    pregunta=0
    respondida = get_object_or_404(PreguntaRespondida, pk=pregunta_respondida_pk)
    preguntas= Pregunta.objects.all().aggregate(nro=Sum('max_puntaje')) #sale un diccionario {a:5}
    no_respuesta = ElegirRespuesta.objects.count()
    # hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    # respuestas = ElegirRespuesta.objects.all()
    for i in preguntas:         
         maximo_puntaje_total=preguntas[i]

    nro_preguntas=Pregunta.objects.count()
    porcentaje=0
    if puntaje_total == 'None':
        puntaje_totall=0  
        porcentaje=0     

    else:        
        puntaje_totall=float(maximo_puntaje_total)
        porcentaje=int(round(((float(puntaje_total)*100)/puntaje_totall),0))

    context = {
        'respondida': respondida,
        'puntaje_total':puntaje_totall,
        'porcentaje': porcentaje,
        
    }
    return render(request, './lecciones/resultados.html', context)



@login_required(login_url="/login/")
def leccion1_2(request):
    id = 2
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()

        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            

            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')

    return render(request, "./lecciones/leccion1.2.html", context)


@login_required(login_url="/login/")
def leccion1_3(request):
    id = 3
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion1.3.html", context)


@login_required(login_url="/login/")
def leccion2(request):
    return render(request, "./lecciones/leccion2.html")


@login_required(login_url="/login/")
def leccion2_1(request):
    id = 4
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion2.1.html", context)


@login_required(login_url="/login/")
def leccion2_2(request):
    id = 5
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion2.2.html", context)


@login_required(login_url="/login/")
def leccion2_3(request):
    id = 6
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion2.3.html", context)

# INICIO leccion 3


@login_required(login_url="/login/")
def leccion3(request):
    return render(request, "./lecciones/leccion3.html")


@login_required(login_url="/login/")
def leccion3_1(request):
    id = 7
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion3.1.html", context)


@login_required(login_url="/login/")
def leccion3_2(request):
    id = 8
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion3.2.html", context)


@login_required(login_url="/login/")
def leccion3_3(request):
    id = 9
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion3.3.html", context)
# FIN leccion 3


# INICIO leccion 4
@login_required(login_url="/login/")
def leccion4(request):
    return render(request, "./lecciones/leccion4.html")


@login_required(login_url="/login/")
def leccion4_1(request):
    id = 10
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)  # He

        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        # preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        logging.debug(
            "**************7*****************Log mpregunta_pk.", pregunta_pk)
        #pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        logging.debug(
            "*******************************Log pregunta_respondida.", pregunta_respondida)
        logging.debug(
            "*******************************Log respuesta_pk.", respuesta_pk)
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk, puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion4.1.html", context)


@login_required(login_url="/login/")
def leccion4_2(request):
    id = 11
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')  
        logging.basicConfig(level=logging.NOTSET)  # He
      
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion4.2.html", context)


@login_required(login_url="/login/")
def leccion4_3(request):
    id = 12
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')  
        logging.basicConfig(level=logging.NOTSET)      
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion4.3.html", context)
# FIN leccion 4


# INICIO leccion 5
@login_required(login_url="/login/")
def leccion5(request):

    return render(request, "./lecciones/leccion5.html")


@login_required(login_url="/login/")
def leccion5_1(request):
    id = 13
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')      
        logging.basicConfig(level=logging.NOTSET)  
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion5.1.html", context)


@login_required(login_url="/login/")
def leccion5_2(request):
    id = 14
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion5.2.html", context)


@login_required(login_url="/login/")
def leccion5_3(request):
    id = 15
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion5.3.html", context)


@login_required(login_url="/login/")
def leccion5_4(request):
    id = 16
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion5.4.html", context)
# FIN leccion 5


# INICIO leccion 6
@login_required(login_url="/login/")
def leccion6(request):

    return render(request, "./lecciones/leccion6.html")


@login_required(login_url="/login/")
def leccion6_1(request):
    id = 17
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion6.1.html", context)


@login_required(login_url="/login/")
def leccion6_2(request):
    id = 18
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion6.2.html", context)


@login_required(login_url="/login/")
def leccion6_3(request):
    id = 19
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
       
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion6.3.html", context)
# FIN leccion 6


# INICIO leccion 7
@login_required(login_url="/login/")
def leccion7(request): 
    return render(request, "./lecciones/leccion7.html")


@login_required(login_url="/login/")
def leccion7_1(request):
    id = 20
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        logging.basicConfig(level=logging.NOTSET)
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion7.1.html", context)


@login_required(login_url="/login/")
def leccion7_2(request):
    id = 21
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')   
        logging.basicConfig(level=logging.NOTSET)     
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion7.2.html", context)


@login_required(login_url="/login/")
def leccion7_3(request):
    id = 22
    QuizUser, created = Usuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')     
        logging.basicConfig(level=logging.NOTSET)   
        pregunta_respondida = QuizUser.intentos.prefetch_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        # pregunta_respondida
        respuesta_pk = request.POST.get('respuesta_pk')       
        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)

        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)
        puntaje_total=QuizUser.obtener_puntaje()
        return redirect('resultado', pregunta_respondida.pk,puntaje_total)
    else:
        try:
            # pregunta=Pregunta.objects.filter(leccion=id).get()
            pregunta = QuizUser.obtener_nuevas_preguntas(id)
            if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

            context = {
                'pregunta': pregunta

            }
        except ObjectDoesNotExist:
            #raise Http404
            return redirect('curso')
    return render(request, "./lecciones/leccion7.3.html", context)
# FIN leccion 7

# INICIO leccion 8
@login_required(login_url="/login/")
def leccion8(request): 
    return render(request, "./lecciones/leccion8.html")