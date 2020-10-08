from django.shortcuts import render, reverse
from authentication.forms import LoginForm, SignupForm
from twitteruser.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class AuthHomeView(View):
    def get(self, request):
        return render(request, 'authentication/auth_home.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
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
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'authentication/signup.html', {'form': form})
 
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            custom_user = CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                full_name=data['full_name'],
            )
            custom_user.save()
        return HttpResponseRedirect(reverse('homepage'))


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('auth_home'))
