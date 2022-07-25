

"""
STEP 1 :
file: website/main/views.py
# We want to redirect to login page when an unlogged user try to access Home page
*************************************************************
"""
from django.contrib.auth.decorators import login_required

# We place the redirection process on top of the required rendering function
@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')
