from django import forms
from .models import *
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
	contact_email=forms.EmailField(required=True)
	class Meta:
		model=Email
		fields=['contact_email']