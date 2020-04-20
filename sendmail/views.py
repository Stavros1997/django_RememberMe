from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Email


# Create your views here.

def index(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['stavros.pgs@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'home.html')

# Contact form view

def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            


            contact_email = request.POST.get('contact_email')
            
            Email.objects.create(**form.cleaned_data)
            template = get_template('blog/contact_form.txt')


            context = {
                
                'contact_email' : contact_email,
                
            }
            
            content = template.render(context)

            email = EmailMessage(
                "RememberMe",
                content,
                "Creative web" + '',
                [contact_email],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            #return redirect('blog:success')
    return render(request, 'blog/contact.html',{'form':Contact_Form})