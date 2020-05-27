from django.shortcuts import render
from tweet.forms import TweetForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def tweetview(request):
    form = TweetForm()
    return render(request, 'tweet/tweet.html', {'form': form})
