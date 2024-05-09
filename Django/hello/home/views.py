from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the home index.")

def about(request):
    return HttpResponse("Hello, world. You're at the home about.")

def services(request):
    return HttpResponse("Hello, world. You're at the home services.")

def contact(request):
    return HttpResponse("Hello, world. You're at the home contact.")
