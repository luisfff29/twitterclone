from django.shortcuts import render
from authentication.forms import LoginForm, SignupForm

# Create your views here.


def loginview(request):
    form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def signupview(request):
    form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})
