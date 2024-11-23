from django.shortcuts import render
from django.http import HttpResponse




def meals(request):
    return HttpResponse('Hi I am Coming')

