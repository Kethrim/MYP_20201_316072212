from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re

def home(request):
    a = []
    aStr = a.__str__()
    return HttpResponse(aStr)

def hola_there(request, name):
    return render(
        request,
        'hola/hola_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )