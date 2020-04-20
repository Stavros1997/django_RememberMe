from django.db import models

# Create your models here.
class Email(models.Model):
	contact_email=models.EmailField()