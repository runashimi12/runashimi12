from django.db import models
from django.contrib.auth.models import User
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
    texto= models.TextField()
    respuesta_p=models.CharField(max_length=255)
    leccion=models.CharField(max_length=255)
    def __str__(self):
        return f'Pregunta {self.id}: {self.texto} {self.respuesta}, {self.leccion} '


class Respuesta(models.Model):
    estudiante=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    Preguntas_k=models.ForeignKey(Pregunta, on_delete=models.SET_NULL, null=True)
    leccion=models.CharField(Pregunta, max_length=255)
    respuesta=models.CharField(max_length=255)
    calificacion=models.CharField(max_length=255)
    def __str__(self):
        return f'Pregunta {self.id}: {self.estudiante} {self.Preguntas} {self.leccion} '
