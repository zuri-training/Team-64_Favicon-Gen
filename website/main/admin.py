from django.contrib import admin
# START:for_download_tuto
from .models import FilesAdmin
# END:for_download_tuto


# Register your models here.

# START:for_download_tuto
admin.site.register(FilesAdmin)
# END:for_download_tuto