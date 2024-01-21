from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Photo


def home(request):
    photos = Photo.objects.all()
    return render(request, "home.html" , {"photos" : photos})


def detail(request, photo_id):
    photo = get_object_or_404(Photo,pk=photo_id)
    return render(request, "detail.html", {"photo" : photo})
