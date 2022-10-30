from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def blog(request):
    return render(request,'blog.html')

def concert(request):
    return render(request,"concert.html")

def contact(request):
    return render(request,"contact.html")

def homewithmyevents(request):
    return render(request,"homewithmyevents.html")

def login(request):
    return render(request,"login.html")

def schedule(request):
    return render(request,"schedule.html")

def screening(request):
    return render(request,"screening.html")

def signup(request):
    return render(request,"signup.html")

def events(request):
    
    return render(request,"events.html")

def theatre(request):
    return render(request,"theatre.html")