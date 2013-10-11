from django import forms
from captcha.fields import CaptchaField
from socios.models import Pais

class ContactForm(forms.Form):
	nombre = forms.CharField(max_length=200)
	correo = forms.EmailField()
	asunto = forms.CharField(max_length=200, required=False)
	mensaje = forms.CharField(required=False, widget=forms.Textarea)
	captcha = CaptchaField()

class PaisForm(forms.Form):
    pais = forms.ModelChoiceField(queryset=Pais.objects.all())
