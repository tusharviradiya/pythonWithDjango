from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET", "POST"])
def hello(request):
    if request.method == "GET":
        print(request.data)
        return Response({"msg": "This is GET request"})
    if request.method == "POST":
        return Response({"msg": "This is POST request"})
