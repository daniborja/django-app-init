from django.http import HttpResponse, JsonResponse

from django.shortcuts import render


# Create your views here.

def helloworld(request):
    return HttpResponse('<h1>Hello</h1>')
