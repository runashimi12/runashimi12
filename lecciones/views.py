from lecciones.models import Respuesta, Usuario
from django.shortcuts import get_object_or_404, render


# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def list_rta(request):
    no_respuesta=Respuesta.objects.count()
    respuestas= Respuesta.objects.all() #hacemos un query para recuperar todos los objetos de tipo Persona en la BD
    return render(request, "./respuestas/list.html",{'no_respuesta':no_respuesta, 'respuestas': respuestas} )


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