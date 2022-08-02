from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesAdmin

# Create your views here.
def home(request):
    # get all objects
    context={'file':FilesAdmin.objects.all()}
    return render (request, 'blog/home.html',context)

def download(request,path):
     # get the download path
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-disposition']='inline;filename=' +os.path.basename(download_path)
            return response
    raise Http404   