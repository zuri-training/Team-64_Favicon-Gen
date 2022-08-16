from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':'text',
            'id':'username',
            'name':'username',
            'placeholder':'Username',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'type':'email',
            'id':'email',
            'name':'email',
            'placeholder':'name@email.com',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':'password',
            'id':'password1',
            'name':'password1',
            'placeholder':'Password',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':'password',
            'id':'password2',
            'name':'password2',
            'placeholder':'Password',
        })
    
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SignInForm(AuthenticationForm):
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



class ForgottenPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ForgottenPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'required':'',
        'type':'email',
        'id':'email',
        'placeholder':'name@email.com'
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'required':'',
            'type':'password',
            'id':'password1',
            'name':'password1',
            'placeholder':'Your password...',
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'required':'',
            'type':'password',
            'id':'password2',
            'name':'password2',
            'placeholder':'Confirm your password...',
    }))