from pyexpat import model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
import random

import logging

# Create your models here.

 
class GrupoClase(models.Model):
    nombre=models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f'{self.nombre}'

# class GrupoDefault(models.Model):
#     grupodefault = GrupoClase()
#     grupodefault.save()

# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('sinGrupo', 'sinGrupo'),
#         ('grupoA', 'grupoA'),
#     ) 
#     grupoClase = models.CharField(max_length = 50, choices = ROLE_CHOICES)


#     def get_grupoclase(self):
#         return getattr(self, self.grupoClase, None)
#     class Meta:
#         app_label='lecciones'


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model= User
#         fields= UserCreationForm.Meta.fields+('grupoClase',)

class Rol(models.Model):
    nombre=models.CharField(max_length=255,null=True)
    def __str__(self):
        return f'Rol: {self.id}: {self.nombre}'



class Pregunta(models.Model):
    NUMER_DE_RESPUESTAS_PERMITIDAS = 1
    texto= models.TextField(verbose_name= 'Texto de la pregunta')
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=5,  decimal_places=2, max_digits=6)
    leccion=models.CharField(max_length=255, null=True, default=1, unique= True )
    def __str__(self):
        return f'P:  {self.texto} {self.max_puntaje}' 
  # respuesta_p=models.CharField(max_length=255, null=True)
    # estudiante=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA=4
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')
    def __str__(self):
        return self.texto 

        # respondidas = PreguntaRespondida.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
    #nombre= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Usuario(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    # rol=models.ForeignKey(Rol, default=1, on_delete=models.SET_NULL, null=True)
    puntaje_total=models.DecimalField(verbose_name='Puntaje total', default=0, null=True, decimal_places=2, max_digits=10)
    grupo = models.ForeignKey(GrupoClase, null=True, on_delete=models.SET_NULL)
 
 
    def crear_intentos(self, pregunta):
        intento = PreguntaRespondida(pregunta=pregunta, quizUser=self)
        intento.save()
 
    def obtener_nuevas_preguntas(self, id):
        respondidas = PreguntaRespondida.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
        #respondidas = PreguntaRespondida.objects.filter(quizUser=self).values_list('pregunta__pk')
        #respondidas = PreguntaRespondida.objects.filter(quizUser=self)
        logging.basicConfig(level=logging.NOTSET) # He
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        pregunta= Pregunta.objects.get(leccion=id)
        #preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        #preguntas_restantes=respondidas.respuesta_seleccionada.correcta
        respondid = PreguntaRespondida.objects.filter(quizUser=self).values('pregunta__pk')
        #if preguntas_restantes.exists():
        #    return None
     
       
        if  respondid.exists():
            if pregunta.id in respondidas:
                return None
        #return random.choice(preguntas_restantes)
        return pregunta
 
    def validar_intento(self, pregunta_respondida, respuesta_selecionada):
        
        if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
            
            return

        pregunta_respondida.respuesta_selecionada = respuesta_selecionada
        if respuesta_selecionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_selecionada
        else:
            pregunta_respondida.respuesta = respuesta_selecionada


        pregunta_respondida.save()
        self.actualizar_puntaje()
        
    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']
        self.puntaje_total = puntaje_actualizado
        self.save()
    def obtener_puntaje(self):
        puntaje_total=self.puntaje_total
        return puntaje_total
    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.usuario}, grupo: {self.grupo}' 
    # class Meta:
    #     ordering = ["-puntaje_total"]
   
class PreguntaRespondida(models.Model):
    quizUser = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta= models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='Es esta la respuesta correcta?', default=False,null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return f'PreguntaRespondida: {self.quizUser}, {self.pregunta}, puntaje obtenido {self.puntaje_obtenido}'  
    

