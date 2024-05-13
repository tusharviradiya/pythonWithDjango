from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_function(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def intoduction(request):
    a = '<h1>My name is Tushar and I am Blockchain Developer</h1>'
    return HttpResponse(a)