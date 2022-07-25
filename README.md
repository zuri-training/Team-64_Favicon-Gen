# 0-my_auth_process.py
#################################################################################################################################################################################
"""
Name of the project : website
Name of the app : main
"""

"""
STEP 1 :
file: website/website/urls.py
*************************************************************
"""
# Add default django urls for authentication
urlpatterns = [
    # ...
    path('', include('django.contrib.auth.urls'))
]





"""
STEP 2 :
file: website/main/templates/main/base.html
# This is the master html file that will define the layout
# of all later pages.
*************************************************************
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    # This title block will have its value changed depending on the displayed page
    <title>{% block title %}My Site{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
</head>
<body>
    # All our displayed pages will have the same navbar
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <div>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="/home" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="/create-post" class="nav-link">Post</a>
                    </li>
                </ul>
            </div>
            <div>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="/login" class="nav-link">Login</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">
        # This content block will have its value changed depending on the displayed page
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>





"""
STEP 3 :
file: website/main/templates/registration/login.html
# It's important to have "login.html" inside "templates/registration/" folder
# So that it can be directly recognized by django urls defined earlier
*************************************************************
"""
# Define the template for login page

# We extend this page from the master html file so that it keeps the same layout
{% extends 'main/base.html' %}
# Our custom title
{% block title %}Login{% endblock %}
# Our custom content
{% block content %}
<div class="container d-flex flex-column justify-content-center mt-5" style="width: 40%;">
    <div class="col mt-5">
        <form action="" method="post">
            # always set in a form to avoid security issues
            {% csrf_token %}
            <table>
                # Django recognizes that this is a login page, then know what inputs 
                # should be displayed in this form so we don't have to do it.
                # However there is a way to do it ourselves.
                {{form.as_table}}
            </table>
            <p>Don't have an account ? Create one <a href="/sign-up">Here</a></p>
            <div class="container d-flex justify-content-center" style="width: 10%;">
                # submit button
                <input type="submit" class="btn btn-primary btn-lg" value="Login" style="margin: 15px;">                
            </div>    
        </form> 
    </div>
</div>
{% endblock %}





"""
STEP 4 :
file: website/website/settings.py
# At the bottom of the file
# Define where to go after login / logout
*************************************************************
"""
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/login'





"""
STEP 5 :
file: website/main/urls.py
# Add path to "home" page
# "login" page path is already define inside django (STEP 1)
*************************************************************
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
]





"""
STEP 6 :
file: website/main/templates/registration/sign_up.html
*************************************************************
"""
# Define the template for sign_up page
# We extend this page from the master html file so that it keeps the same layout
{% extends 'main/base.html' %}
# Our custom title
{% block title %}Login{% endblock %}
# Our custom content
{% block content %}
<div class="container d-flex flex-column justify-content-center mt-5" style="width: 100%;">
    <div class="col mt-5">
        <form action="" method="post">
            # always set in a form to avoid security issues
            {% csrf_token %}
            <table>
                # Django recognizes that this is a SIGN_UP page, then know what inputs 
                # should be displayed in this form so we don't have to do it.
                # However there is a way to do it ourselves.
                {{form.as_table}}
            </table>
            <p>Have an account ? Login <a href="/login">Here</a></p>
            <div class="" style="width: 10%;">
                # submit button
                <input type="submit" class="btn btn-primary btn-lg" value="Register" style="margin: 15px;">                
            </div>    
        </form> 
    </div>
</div>
{% endblock %}





"""
STEP 7 :
file: website/main/views.py
# Define the function to render sign_up page
# Login rendering is managed by django (STEP 1)
*************************************************************
"""
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

def sign_up(request):
    if request.method == 'POST':
        # When we submmit the form
        form = RegisterForm(request.POST)
        if form.is_valid():
            # When user informations are valid
            # Save the user
            user = form.save()
            # Login the user
            login(request, user)
            # Redirect to home page
            return redirect('/home')
    else:
        # When we enter the empty sign_up page (method == 'GET')
        form = RegisterForm()
    
    # When rendering sign_up page, we pass form object to it as "form".  --->  {"form":form}
    return render(request, 'registration/sign_up.html', {"form":form})





"""
STEP 8 :
file: website/main/forms.py
# Define the RegisterForm class
*************************************************************
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # We define this field specifically because it is not set by default from Django
    email = forms.EmailField(required=True)

    class Meta:
        # The DB model we are interacting with in our form
        model = User
        # The fields to be present in our form
        fields = ["username", "email", "password1", "password2"]





"""
STEP 9 :
file: website/main/urls.py
# Add path to "sign_up" page
*************************************************************
"""
from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('sign-up', views.sign_up, name="sign_up"),
]




# 1-display_logged_username_process.py
#################################################################################################################################################################################


"""
STEP 1 :
file: website/main/templates/main/base.html
# This is the master html file that will define the layout
# of all later pages.
*************************************************************
"""
# ...
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <div>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="/home" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="/create-post" class="nav-link">Post</a>
                    </li>
                </ul>
            </div>
            <div>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    # Logged User username
                    <span class="navbar-text">Logged in as {{user.username}}  | </span>
                    <li class="nav-item">
                        <a href="/logout" class="nav-link">Logout</a>
                    </li>

                    {% else %}

                    <li class="nav-item">
                        <a href="/login" class="nav-link">Login</a>
                    </li>

                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
# ...





# 2-redirect_unlogged_user_process.py
#################################################################################################################################################################################


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
