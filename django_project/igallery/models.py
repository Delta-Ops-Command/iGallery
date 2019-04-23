from django.db import models
from django.contrib.auth.models import User


class UploadImage(models.Model):
    # Includes uploaded image, and the use that uploads it, 
    # ... the time it's been created and updated. Why updated? I honestly don't know.
    objects = models.Manager()
    # UploadImage should use the same 
    file_field = models.ImageField(upload_to='cats/')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "upload_image_model"
        # permissions...