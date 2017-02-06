from django import forms
from django.core import validators
from restaurantes.models import Restaurantes
import requests
class formAdd(forms.Form):
	nombre = forms.CharField(max_length=65,widget=forms.TextInput({'class': 'form-control', "placeholder": "Introduzca nombre del restaurante"}),required=True)
	ciudad = forms.CharField(max_length=65,widget=forms.TextInput({'class': 'form-control', "placeholder": "Introduzca nombre de la ciudad"}),required=True)
	codigo_postal = forms.IntegerField(widget=forms.NumberInput({ 'class': 'form-control',"placeholder": "Introduzca el codigo postal"}),required=True)
	id_restaurante = forms.CharField(widget=forms.HiddenInput(),required=False)
	def clean_codigo_postal(self):
		r= requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+self.cleaned_data.get('ciudad', '')+'+'+str(self.cleaned_data.get('codigo_postal', ''))+'&key=AIzaSyCJ3cz5yCNHDgQUUS_cteeyRffpSUIbjTQ')
		h= r.json()
		if (h['results'][0]['address_components'][0]['types'][0]!="postal_code"):

		    raise forms.ValidationError("El codigo postal no pertenece a "+self.cleaned_data.get('ciudad', '')+".")

		return self.cleaned_data.get('codigo_postal', '')
	def save(self):
		resta=Restaurantes()
		return resta.add(self.cleaned_data)
	def update(self):
		resta=Restaurantes()
		return resta.modificar(self.cleaned_data)
