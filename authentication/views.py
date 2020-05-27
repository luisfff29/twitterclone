from django.shortcuts import render, reverse
from authentication.forms import LoginForm, SignupForm
from twitteruser.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def signupview(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                is_staff=True,
                is_superuser=True
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
