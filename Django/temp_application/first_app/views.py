from django.shortcuts import render

# Create your views here.
def hello_fun(requrest):
    return render(requrest, "course/index.html")
