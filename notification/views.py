from django.shortcuts import render
from notification.models import NotificationModel
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


# Create your views here.
class NotificationView(LoginRequiredMixin, View):
    def get(self, request):
        num_tweets = TweetMessage.objects.filter(
            user=CustomUser.objects.get(username=request.user.username))
        tweets = NotificationModel.objects.filter(
            user=request.user, viewed=False)
        num_notif = tweets.count()
        for tweet in tweets:
            tweet.viewed = True
            tweet.save()
        return render(request, 'notification/notification.html', {
            'num_tweets': num_tweets.count(),
            'tweets': tweets,
            'num_notif': num_notif
        })
