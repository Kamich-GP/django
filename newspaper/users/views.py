from django.shortcuts import render

# Create your views here.

def bla(request):
    return render(request, 'templates/home.html')
