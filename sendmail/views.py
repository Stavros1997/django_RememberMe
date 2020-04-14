from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['stavros.pgs@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'home.html')
