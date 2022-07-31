from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

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


def success(request):
	return HttpResponse('successfully uploaded')
