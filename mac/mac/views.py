from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    a = 5
    c = 10
    d = 15
    e =a+c+d
    return HttpResponse("<h1>Hello my index total is: "+str(e)+"</h1>")
