from django.forms import ModelForm
from lecciones.models import Respuesta

class RespuestaForm(modelsForm):
	class Meta:
		model = Respuesta   #la clase de modelo que vamos a utilizar
		fields='__all__'  #vamos a utilizar todos los atributos de nuestro modelo de tipo persona
		widgets= {   #cual va hacer el tipo de campo del tipo de persona el cual es un diccionario
						 #tipo email par qeu tenga un formato 
			}