from django.shortcuts import render
from notification.models import NotificationModel
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


# Create your views here.
class NotificationView(LoginRequiredMixin, View):
    def get(self, request):
        tweets = TweetMessage.objects.filter(user=request.user)
        tweets_notif = NotificationModel.objects.filter(
            user=request.user, viewed=False)
        num_notif = tweets_notif.count()
        for tweet in tweets_notif:
            tweet.viewed = True
            tweet.save()
        return render(request, 'notification/notification.html', {
            'tweets_notif': tweets_notif,
            'tweets': tweets,
            'num_notif': num_notif
        })
