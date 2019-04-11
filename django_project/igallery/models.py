from django.db import models

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = "pictures")

    class Meta:
        db_table = "imageModel"