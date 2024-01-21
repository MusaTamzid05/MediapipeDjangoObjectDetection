from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photo")
    processed_image = models.ImageField(default="black.jpg")

    def __str__(self):
        return self.title

