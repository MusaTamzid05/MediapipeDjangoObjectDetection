from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings

from typing import Optional
from .models import Photo

from.utils import Detector
from.utils import save_processed_image

detector: Optional[Detector] = None


def home(request):
    photos = Photo.objects.all()
    return render(request, "home.html" , {"photos" : photos})


def detail(request, photo_id):
    photo = get_object_or_404(Photo,pk=photo_id)
    return render(request, "detail.html", {"photo" : photo})


def process_image(request, photo_id):
    global detector
    photo = get_object_or_404(Photo, pk=photo_id)
    image_path = str(settings.BASE_DIR) + photo.image.url




    if detector is None:
        detector = Detector()

    detection_results = detector.detect(image_path=image_path)
    result_image = detector.visualize(
            image_path=image_path,
            detection_results=detection_results
            )

    print(result_image)
    photo.processed_image = save_processed_image(
            image_mat=result_image,
            instance=photo,
           )

    return redirect("detail", photo_id=photo_id)
