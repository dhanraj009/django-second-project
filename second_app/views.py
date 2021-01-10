from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Child branch change")

# Create your views here.
