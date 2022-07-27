from django.db import models

# Create your models here.

# START:for_download_tuto
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
# END:for_download_tuto
