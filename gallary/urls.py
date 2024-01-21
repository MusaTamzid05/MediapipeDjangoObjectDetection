from . import views
from django.urls import path

urlpatterns = [
        path("", views.home, name="home"),
        path("detail/<int:photo_id>", views.detail, name="detail"),
        path("process_image/<int:photo_id>", views.process_image, name="process_image"),
        ]
