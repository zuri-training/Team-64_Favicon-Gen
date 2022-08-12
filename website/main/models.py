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
    saved_to_drafts = models.BooleanField(default=False)

class GeneratedFavicon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zip_file = models.ForeignKey(FaviconZipFile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.FileField (upload_to="generator/" ,null=True, blank=True)
    img_type = models.CharField(max_length=255)
    size = models.IntegerField(null=True)
    saved_to_drafts = models.BooleanField(default=False)
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
    size = models.IntegerField(null=True)
    saved_to_drafts = models.BooleanField(default=False)
    html_code = models.CharField(max_length=255)
    
class Texticons(models.Model):
    name = models.CharField(max_length=255)
    img_path = models.FileField (upload_to="texticons/images/" ,null=True, blank=True)
    zip_path = models.FileField (upload_to="texticons/zipfiles/" ,null=True, blank=True)
    img_type = models.CharField(max_length=255)
    html_code = models.CharField(max_length=255, default="")

class UserTexticon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE ,null=True, blank=True, default = None)
    texticon = models.ForeignKey(Texticons, on_delete=models.CASCADE ,null=True, blank=True, default = None)
    saved_to_drafts = models.BooleanField(default=False)