from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("<h1> Contact me </h1>")


def blog(request):
    return HttpResponse("<h1> Blog page </h1>")
