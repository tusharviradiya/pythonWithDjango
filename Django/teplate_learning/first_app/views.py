from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_fun(requrest):
    courcename = {'fname':'tushar'}
    return render(requrest, "first/first_template.html", context=courcename)