from django.shortcuts import render
from notification.models import NotificationModel
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def notificationview(request):
    num_tweets = TweetMessage.objects.filter(
        user=CustomUser.objects.get(username=request.user.username)).count()
    tweets = NotificationModel.objects.filter(user=request.user, viewed=False)
    for tweet in tweets:
        tweet.viewed = True
        tweet.save()
    return render(request, 'notification/notification.html', {
        'num_tweets': num_tweets,
        'tweets': tweets
    })
