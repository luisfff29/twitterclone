from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Password',
            'type': 'password'
        }
    ))


class SignupForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Full Name'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Email',
            'type': 'email'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-tweet text-white border-0',
            'placeholder': 'Password',
            'type': 'password'
        }
    ))
