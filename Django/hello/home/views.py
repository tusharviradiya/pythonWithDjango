from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the home index.")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("Hello, world. You're at the home about.")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("Hello, world. You're at the home services.")

def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("Hello, world. You're at the home contact.")
