from django.shortcuts import render
from tweet.forms import TweetForm


# Create your views here.
def tweetview(request):
    form = TweetForm()
    return render(request, 'tweet/tweet.html', {'form': form})
