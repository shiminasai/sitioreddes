from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	nombre = forms.CharField(max_length=200)
	correo = forms.EmailField()
	asunto = forms.CharField(max_length=200, required=False)
	mensaje = forms.CharField(required=False, widget=forms.Textarea)
	captcha = CaptchaField()