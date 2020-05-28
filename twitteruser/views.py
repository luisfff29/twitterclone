from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage
from twitteruser.models import CustomUser


# Create your views here.
@login_required
def index(request):
    tweets = TweetMessage.objects.all().order_by('-date')
    profile_path = '/profile/' + request.user.username
    return render(request, 'twitteruser/index.html', {'tweets': tweets, 'profile_path': profile_path})


@login_required
def profile(request, name):
    user = CustomUser.objects.get(username=name)
    tweets = TweetMessage.objects.filter(user=user).order_by('-date')
    return render(request, 'twitteruser/profile.html', {'tweets': tweets, 'profile_name': name})
