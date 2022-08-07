from pathlib import Path
import zipfile

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FaviconForm
from .models import Favicon

# Create your views here.
def favicon_image_view(request):
	if request.method == 'POST':
		form = FaviconForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = FaviconForm()
	return render(request, 'favicon_image_form.html', {'form' : form})


def upload_success_view(request):
	return HttpResponse('successfully uploaded')


# @login_required
def download_favicon_view(request, slug):
  """This endpoint returns the favicon & embeds as a zip file for a favicon project."""
  try:
        favicon = Favicon.objects.get(slug=slug)
  except Favicon.DoesNotExist:
    raise Http404('Favicon does not exist!')
      
  response = HttpResponse(content_type='application/zip')
  zf = zipfile.ZipFile(response, 'w')

    # add the embed.html
  embed_str = f"""
  <link rel="icon" type="image/x-icon" href="{favicon.icon_Img.name}">
    """
  zf.writestr('embed.html', embed_str)

    # add the favicon image.
  zf.write(favicon.icon_Img.path, Path(favicon.icon_Img.path).name)
    
    # return the zip file
  response['Content-Disposition'] = f'attachment; filename=favicon_gen.zip'
  
  return render(request, 'result.html', {'embed_str' : embed_str})
