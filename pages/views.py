from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})
	
def sign_up_view(request, *args,**kwargs):
	return render(request,'sign_up.html',{})