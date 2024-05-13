from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function_two(request):
    return HttpResponse("hello, this is second application's function")
