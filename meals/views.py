from django.shortcuts import render
from django.http import HttpResponse




def meal(request):
    return HttpResponse('Hi I am Coming')

