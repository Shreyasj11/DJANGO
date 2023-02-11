from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainwindow(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/app1_home'>link to Registration page</a>  <br> <h2> link to home page </h2>")
