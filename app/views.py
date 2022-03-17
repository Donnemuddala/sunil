from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dhoni(request):
    return HttpResponse('<marquee><h1>dhoni is best captain</h1></marquee>')
def jaddu(request):
    return HttpResponse('<marquee><h2>good all arounder<h2></marquee>')
def pushpa(request):
    return HttpResponse('<i>king of redwood </i>') 
