from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Shop index</h1>")


def about(request):
    return HttpResponse("We are at about")


def contact(request):
    return HttpResponse("We are at contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def productView(request):
    return HttpResponse("We are at product view")


def checkout(request):
    return HttpResponse("We are at checkout")
