from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':'text',
            'id':'username',
            'placeholder':'Username',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'type':'email',
            'id':'email',
            'placeholder':'name@email.com',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':'password',
            'id':'password1',
            'placeholder':'Password',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':'password',
            'id':'password2',
            'placeholder':'Password',
        })
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SignInForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':'text',
            'id':'username',
            'name':'username',
            'placeholder':'Your username...',
        })
        self.fields["password"].widget.attrs.update({
            'required':'',
            'type':'password',
            'id':'password',
            'name':'password',
            'placeholder':'Your password...',
        })

    class Meta:
        model = User
        fields = ["username", "password"]