from django.contrib import admin
from django.urls import path, re_path
from app1_home import views
#from app1_home import views
#from django.conf.urls import include
# these 2 ARE REMOVED BECAUSE WE ARE IN THE APP FOLDER ONLY
urlpatterns = [
    re_path(r'^$', views.welcome,name='welcome'),
    #re_path(r'^$app1_home',include('app1_home'))
]
