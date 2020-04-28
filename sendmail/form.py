from django import forms
from .models import *
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
	contact_email=forms.EmailField(required=True)
	class Meta:
		model=Email
		fields=['contact_email']

	def clean_contact_email(self,*args,**kwargs):
		contact_email= self.cleaned_data.get('contact_email')

        # Check to see if any users already exist with this email as a username.
		try:
			match = Email.objects.get(contact_email=contact_email)
		except Email.DoesNotExist:
            # Unable to find a user, this is fine
			return contact_email

        # A user was found with this as a username, raise an error.
		raise forms.ValidationError('This email address is already in use.')