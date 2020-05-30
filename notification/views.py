from django.shortcuts import render
from notification.models import NotificationModel
from tweet.models import TweetMessage
from twitteruser.models import CustomUser


# Create your views here.
def notificationview(request):
    num_tweets = TweetMessage.objects.filter(
        user=CustomUser.objects.get(username=request.user.username)).count()
    return render(request, 'notification/notification.html', {'num_tweets': num_tweets})
