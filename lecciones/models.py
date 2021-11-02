from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import Random
# Create your models here.

class Rol(models.Model):
    nombre=models.CharField(max_length=255)
    def __str__(self):
        return f'Rol {self.id}: {self.nombre}'

class Usuario(models.Model):
    nombre= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Usuario {self.id}: {self.nombre}  {self.rol} '


class Pregunta(models.Model):
    NUMER_DE_RESPUESTAS_PERMITIDAS=1 
    texto= models.TextField(verbose_name= 'Texto de la pregunta')
    # respuesta_p=models.CharField(max_length=255, null=True)
    max_puntaje=models.DecimalField(verbose_name='Maximo PUntaje', default=3, decimal_places=2, max_digits=6)
    leccion=models.CharField(max_length=255)
    def __str__(self):
        return f'Pregunta {self.id}: {self.texto} {self.leccion} '


class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA=4
    # estudiante=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    pregunta=models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    # respuesta=models.CharField(max_length=255, null=True)
    correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
    texto=models.TextField(verbose_name='Texto de la respuesta')
    def __str__(self):
        return f'Pregunta {self.id}:   {self.texto} '

class PreguntaRespondida(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta= models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='Es esta la respuesta correcta?', default=False,null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
           


""" class QuizUsuario(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_place=2, max_digits=0)
       
    def crear_intentos(self, pregunta):
        intento=PreguntaRespondida(pregunta=pregunta, quizUser=self)
        intento.save()
    def obtener_nuevas_preguntas(self):
        respondidas = PreguntaRespondida.objects.filter(quizUser=self).values_list('pregunta__pk, flat=True') #part9
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return Random.choice(preguntas_restantes)
    
    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida_pregunta_id != respuesta_seleccionada.pregunta_id:
            return 
            
        pregunta_respondida.respuesta_seleccionada= respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta= True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada
        pregunta_respondida.save()
        self.actualizar_puntaje()

class PreguntaRespondida(models.Model):
    quizUser= models.ForeignKey(QuizUsuario, on_delete=models.CASCADE, related_name="intentos")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta= models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='Es esta la respuesta correcta?', default=False,null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
    
    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']
        self.puntaje_total=puntaje_actualizado
        self.save()  """