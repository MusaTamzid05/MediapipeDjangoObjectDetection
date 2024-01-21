from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo


def home(request):
    photos = Photo.objects.all()
    return render(request, "home.html" , {"photos" : photos})
    
