from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage
from twitteruser.models import CustomUser


# Create your views here.
@login_required
def index(request):
    tweets = TweetMessage.objects.all().order_by('-date')
    return render(request, 'twitteruser/index.html', {'tweets': tweets})


@login_required
def profile(request, name):
    person = CustomUser.objects.get(username=name)
    tweets = TweetMessage.objects.filter(user=person).order_by('-date')
    return render(request, 'twitteruser/profile.html', {'tweets': tweets})
