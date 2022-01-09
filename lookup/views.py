from django.shortcuts import render

# Create your views here.


#typing in website URL = making a REQUEST to the server to bring up the webpage
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})
