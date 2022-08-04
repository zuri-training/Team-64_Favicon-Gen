from django.db import models
from django.conf import settings
# Create your models here.

# START:for_download_tuto
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
# END:for_download_tuto


class FaviconZipFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.FileField (upload_to="generator/" ,null=True, blank=True)

class GeneratedFavicon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zip_file = models.ForeignKey(FaviconZipFile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.FileField (upload_to="generator/" ,null=True, blank=True)
    img_type = models.CharField(max_length=255)
    html_code = models.CharField(max_length=255)


class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.ImageField (upload_to="uploaded/" ,null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.path.delete()
        super().delete(*args, **kwargs)

class ConvertedFavicon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zip_file = models.ForeignKey(FaviconZipFile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.FileField (upload_to="converter/" ,null=True, blank=True)
    img_type = models.CharField(max_length=255)
    html_code = models.CharField(max_length=255)