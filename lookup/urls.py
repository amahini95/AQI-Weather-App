#from django.contrib import admin
from django.urls import path
from . import views

#Creating webpages in Django
#1. URL: somewhere to point webpage to
#2. Actual HTML page itself, usually a template
#3. Need a view.py: brains behind the scenes, lets us use Python in our app

urlpatterns = [
    #path('admin/', admin.site.urls),
    #Every time we make a new webpage, need to add URL here that defines it
    path('', views.home, name="home"),
    path('about', views.about, name="about")
]