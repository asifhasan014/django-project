from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    params ={'name':'asif','designation':'engineer','address':'mohammadpur'}
    return render(request,'index.html',params)
