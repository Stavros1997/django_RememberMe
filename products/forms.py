from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title= forms.CharField(label='',
			widget=forms.TextInput(attrs={"placeholder":"Your title"}))
	email=forms.EmailField()
	description=forms.CharField(required=False,
								widget=forms.Textarea(attrs={
									"placeholder":"Your description",
									"class":"new-class-name two",
									"id":"my-id-for-textarea",
									"rows":20,
									"cols":120
									}
								)
							)
	price=forms.DecimalField(initial=199.99)

	class Meta:
		model=Product
		fields=[
		'title',
		'description',
		'price'


		]
	def clean_email(self,*args,**kwargs):
		# Get the email
		description= self.cleaned_data.get('description')

        # Check to see if any users already exist with this email as a username.
		try:
			match = Product.objects.get(description=description)
		except Product.DoesNotExist:
            # Unable to find a user, this is fine
			return description

        # A user was found with this as a username, raise an error.
		raise forms.ValidationError('This description already in use.')


#class RawProductForm(forms.Form):
#	title=forms.CharField()
#	description=forms.CharField()
#	price=forms.DecimalField()