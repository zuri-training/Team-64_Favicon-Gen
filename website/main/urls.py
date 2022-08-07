from django.urls import path, re_path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('generator_page', views.generatorPage, { 'document_root': settings.MEDIA_ROOT }, name="generator_page"),
    path('converter_page', views.converterPage, { 'document_root': settings.MEDIA_ROOT }, name="converter_page"),
    path('drafts', views.drafts,{ 'document_root': settings.MEDIA_ROOT }, name="drafts"),
    path('sign-up', views.sign_up, name="sign_up"),

    # path('success', views.success, name = 'success'),
    # path('success/<str:filelink>', views.success, name = 'success'),
    re_path(r'^success/(?P<filelink>[-\w]*)/$', views.success, name='success'),
    path('error_w', views.error_w, name = 'error_w'),
]