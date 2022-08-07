# forms.py
from django import forms
from .models import Favicon

class FaviconForm(forms.ModelForm):

	class Meta:
		model = Favicon
		fields = ['name', 'icon_Img']

# this was a (failed) attempt at including svg files for upload. I will keep trying.       
# from django.forms import ModelForm, FileField

# class FaviconForm(ModelForm):
#     class Meta:
#         model = Favicon
#         exclude = []
#         field_classes = {
#             'image': FileField,
#         }

# @admin.register(Favicon)
# class TemplatesAdmin(admin.ModelAdmin):
#     form = FaviconForm