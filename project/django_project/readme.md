# How to reset forgotten password with django
This involves, linking the forgotten password page to a backend(django).

# updated files
The appropriate files were updated and the necessary templates created.

# SMTP configuration
This is a filebase model. This just means that a SMTP Sever hasn't been linked yet, rather the recovery email is being sent on a folder in the django folder called sent_email.
once a sever is set up, the following configuration is needed in settings.py, for it to be effective;

# SMTP email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.getenv('EMAIL_USER')) 
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_PASSWORD'))

Note: if the email and password is not hidden, then it is placed like this = 'email' and 'password'.
# meaning
EMAIL_BACKEND is the SMTP backend that Email will be sent through.
EMAIL_HOST is the host to use for sending email.
EMAIL_USE_TLS - Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587.
EMAIL_PORT - Port to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are username and password to use for the SMTP server respectively.

# more information
more information can be gotten here, for smtp configuration.
https://docs.djangoproject.com/en/4.0/ref/settings/#default-from-email
https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html