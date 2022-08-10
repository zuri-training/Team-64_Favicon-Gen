from django.urls import path, re_path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('reviews', views.reviews, name="reviews"),
    path('tutorial', views.tutorial, name="tutorial"),
    path('texticons', views.texticons, name="texticons"),


    path('generator_page', views.generatorPage, name="generator_page"),    
    path('favicon_generation', views.faviconGeneration, { 'document_root': settings.MEDIA_ROOT }, name="favicon_generation"),
    path('converter_page', views.converterPage, name="converter_page"), 
    path('favicon_conversion', views.faviconConversion, { 'document_root': settings.MEDIA_ROOT }, name="favicon_conversion"),
    path('drafts', views.drafts, { 'document_root': settings.MEDIA_ROOT }, name="drafts"),
    re_path(r'^delete_favicon/(?P<value>\d+)/$', views.deleteFavicon, name="delete_favicon"), 
    
    # Auth
    path('login', views.sign_in, name="login"),
    path('sign-up', views.sign_up, name="sign_up"),
   
    # Status msg
    re_path(r'^success/(?P<filelink>[-\w]*)/$', views.success, name='success'),
    path('error_w', views.error_w, name = 'error_w'),
]