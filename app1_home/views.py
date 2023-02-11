from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(Request):
    #my_dict ={ 'insert_me':"iam comming from views.py file of app1"}
    my_dict = {'insert_me': "iam comming from sub-folder app1"}
    return render (Request, 'app1_home/reg.html', context=my_dict)
   # return HttpResponse("<h1 style='background:pink'> hello! all this is my first django app </h1>")

