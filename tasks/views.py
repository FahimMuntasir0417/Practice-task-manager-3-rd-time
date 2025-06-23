from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from the tasks app!")

def home2(request):
    return HttpResponse("Welcome to the Home page!")

def about(request):
    return HttpResponse("This is the About page.")

def contact(request):
    return HttpResponse("Contact us at contact@example.com.")