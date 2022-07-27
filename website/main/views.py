from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# START:for_download_tuto
from .models import FilesAdmin
# END:for_download_tuto
# Create your views here.

@login_required(login_url="/login")
def home(request):
    # START:for_download_tuto
    context = {'file':FilesAdmin.objects.all()}
    return render(request, 'main/home.html', context)
    # END:for_download_tuto

# START:for_download_tuto
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'ro') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    
    raise Http404
# END:for_download_tuto

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})