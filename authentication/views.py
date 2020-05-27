from django.shortcuts import render
from authentication.forms import LoginForm

# Create your views here.


def index(request):
    form = LoginForm()
    return render(request, 'authentication/index.html', {'form': form})
