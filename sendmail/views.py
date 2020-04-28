from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Email
from django.contrib import messages


# Create your views here.



# Contact form view

def Contact(request):
    Contact_Form = ContactForm
    form=Contact_Form(request.POST or None)
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            messages.success(request, 'Thank you for subscribing')


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
                "RememberMe" + '',
                [contact_email],
                headers = { 'Reply To': contact_email }
            )

            email.send()
    context={
        'form':form

    }
            #return redirect('blog:success')
    return render(request, 'blog/contact.html',context)