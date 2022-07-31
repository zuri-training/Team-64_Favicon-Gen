from django.db import models

# Create your models here.
# models.py
class Favicon(models.Model):
	# name = models.CharField(max_length=50)
	icon_Image = models.ImageField(upload_to='images/')