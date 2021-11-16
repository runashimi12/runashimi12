from django.forms import ModelForm
from lecciones.models import ElegirRespuesta, Pregunta
from django import forms
from .models import ElegirRespuesta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
""" class RespuestaForm(modelsForm):
	class Meta:
		model = ElegirRespuesta   #la clase de modelo que vamos a utilizar
		fields='__all__'  #vamos a utilizar todos los atributos de nuestro modelo de tipo persona
		widgets= {   #cual va hacer el tipo de campo del tipo de persona el cual es un diccionario
						 #tipo email par qeu tenga un formato 
			} """

class ELegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self): #limpiar
		super(ELegirInlineFormset, self).clean()
		
		respuesta_correcta=0
		for formulario in self.forms:
			if not formulario.is_valid():
				return
			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1
		try:
			assert respuesta_correcta == Pregunta.NUMER_DE_RESPUESTAS_PERMITIDAS
		except AssertionError:
			raise forms.ValidationError('solo una respuesta es permitida')
		

