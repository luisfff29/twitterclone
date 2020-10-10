from django.shortcuts import render, reverse
from authentication.forms import LoginForm, SignupForm
from twitteruser.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
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
            messages.error(request, "Invalid username or password.")
            return HttpResponseRedirect(reverse('login'))
        messages.error(request, "Invalid form. Please refresh the page.")
        return HttpResponseRedirect(reverse('login'))


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'authentication/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                custom_user = CustomUser.objects.create_user(
                    username=data['username'],
                    password=data['password'],
                    email=data['email'],
                    full_name=data['full_name'],
                )
            except:
                messages.error(request, "Username or email already taken.")
                return HttpResponseRedirect(reverse('signup'))
            custom_user.save()
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
        messages.error(request, "Invalid fields. Please try again.")
        return HttpResponseRedirect(reverse('signup'))


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('auth_home'))
