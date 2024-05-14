from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_fun(requrest):
    return render(requrest, "first_template.html")