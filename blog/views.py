from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view, class based view

def home(request):
    return HttpResponse("HOME")

def index(request):
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request, 'aboutus.html')

def contactUs(request):
    name = "Tirth"
    email = "tirthmpatel81@gmail.com"
    return render(request, 'blog/contactus.html', {'name':name, 'email':email})

def feedback(request):
    userName = "Tirth Patel"
    userEmail = "tirth812002@gmail.com"
    context = {
        'userName': userName,
        'userEmail': userEmail,
    }
    return render(request, 'blog/feedback.html', context)
