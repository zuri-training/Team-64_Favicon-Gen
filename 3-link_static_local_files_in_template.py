

"""
STEP 1 :
file: website/website/urls.py
*************************************************************
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # ...
]
# Add django static files urls
urlpatterns += staticfiles_urlpatterns()





"""
STEP 2 :
file: website/website/settings.py
*************************************************************
"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# Our static folder that will contain all our css, js, images is named assets (we can choose a random name)
STATICFILES_DIRS= [os.path.join(BASE_DIR,'assets'),]





"""
STEP 3 :
file: website/main/templates/main/base.html
# This is the master html file that will define the layout
# of all later pages.
*************************************************************
"""
# Add your local in the master template
# In the <head> tag
# ...
{% load static %}

    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
# ...

# Or elsewhere
<body>
# ...
# ...
# ...
    <script src="{% static 'js/jquery-2.2.4.min.js' %}"></script>

    <script src="{% static 'js/popper.min.js' %}"></script>

    <script src="{% static 'js/bootstrap.min.js' %}"></script>
</body>