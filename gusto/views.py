from django.http import HttpResponse
from django.shortcuts import render, redirect


def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def base(request):
    return render(request, 'base.html')
