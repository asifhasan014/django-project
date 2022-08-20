from django.http import HttpResponse
from django.shortcuts import render
from django import *


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dtext = request.GET.get('text', 'default')
    dcheck = request.GET.get('removepunc', 'off')
    print(dtext)
    print(dcheck)
    if dcheck == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': 'yo did not ask to remove punctuation'}
        return render(request, 'analyze.html', params)
