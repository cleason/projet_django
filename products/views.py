from contextvars import Context
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, *args, **kwargs):
    name = "Cleason"
    number = 33
    my_list = [3,35,6,7,9]
    context = {
        'nom':name,
        'numero':number,
        'maList':my_list
    }
    return render(request, 'index.html', context)

def contact(request):
    return HttpResponse("<h1> Contact me </h1>")


def blog(request):
    return HttpResponse("<h1> Blog page </h1>")
