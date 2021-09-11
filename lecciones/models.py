from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=255)
    apellido= models.CharField(max_length=255)
    mail=models.CharField(max_length=255)


class Pregunta(models.Model):
    texto= models.TextField()
    respuesta=models.CharField(max_length=255)

class Respuesta(models.Model):
    estudiante=models.CharField(max_length=255)
    Preguntas=models.CharField(max_length=255)
    calificacion=models.CharField(max_length=255)


def __str__(self):
    return f'Pregunta {self.id}: {self.texto} {self.respuesta}'
