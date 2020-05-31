from django.shortcuts import render, reverse
from tweet.forms import TweetForm
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from notification.models import NotificationModel
import re


# Create your views here.
@login_required
def tweetview(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            msg = TweetMessage.objects.create(
                user=CustomUser.objects.get(username=request.user.username),
                body=data['body'],
            )
            users = re.findall(r'@\S+', msg.body)
            if users:
                for i in users:
                    try:
                        if CustomUser.objects.get(username=i[1:]):
                            NotificationModel.objects.create(
                                user=CustomUser.objects.get(username=i[1:]), tweet=msg)
                    except CustomUser.DoesNotExist:
                        continue

        return HttpResponseRedirect(reverse('homepage'))

    num_tweets = TweetMessage.objects.filter(
        user=CustomUser.objects.get(username=request.user.username)).count()
    form = TweetForm()
    return render(request, 'tweet/tweet.html', {'form': form, 'num_tweets': num_tweets})


def tweetdetail(request, id):
    tweet = TweetMessage.objects.get(id=id)
    num_tweets = TweetMessage.objects.filter(user=tweet.user).count()
    profile_user = tweet.user
    return render(request, 'tweet/detail.html', {
        'tweet': tweet,
        'num_tweets': num_tweets,
        'profile_user': profile_user
    })
