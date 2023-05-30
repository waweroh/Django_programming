#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloWorld(request): 
    return HttpResponse('<b>Welcome to my Django app!</b>')