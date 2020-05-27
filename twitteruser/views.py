from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage


# Create your views here.
@login_required
def index(request):
    data = TweetMessage.objects.all()
    return render(request, 'twitteruser/index.html', {'data': data})
