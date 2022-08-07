import secrets

from django.db import models
from django.utils.text import slugify
# Create your models here.
# models.py
class Favicon(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=100)
	icon_Img = models.ImageField(upload_to='images/')
	
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.name) + '-' + secrets.token_hex(3)
		super().save(*args, **kwargs)
