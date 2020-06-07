from django.shortcuts import render, reverse
from tweet.forms import TweetForm
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.http import HttpResponseRedirect
from notification.models import NotificationModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
import re


# Create your views here.
class TweetView(LoginRequiredMixin, View):
    def get(self, request):
        num_tweets = TweetMessage.objects.filter(
            user=CustomUser.objects.get(username=request.user.username))
        num_notif = NotificationModel.objects.filter(
            user=request.user, viewed=False).count()
        form = TweetForm()
        return render(request, 'tweet/tweet.html', {
            'form': form,
            'num_tweets': num_tweets.count(),
            'num_notif': num_notif
        })

    def post(self, request):
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
                                user=CustomUser.objects.get(username=i[1:]),
                                tweet=msg)
                    except CustomUser.DoesNotExist:
                        continue

        return HttpResponseRedirect(reverse('homepage'))


class TweetDetail(View):
    def get(self, request, id):
        tweet = TweetMessage.objects.get(id=id)
        num_tweets = TweetMessage.objects.filter(user=tweet.user).count()
        profile_user = tweet.user
        try:
            num_notif = NotificationModel.objects.filter(
                user=request.user, viewed=False).count()
            following = profile_user in CustomUser.objects.get(
                username=request.user.username).following.all()
        except TypeError:
            num_notif = 0
            following = False

        return render(request, 'tweet/detail.html', {
            'tweet': tweet,
            'following': following,
            'num_tweets': num_tweets,
            'profile_user': profile_user,
            'num_notif': num_notif
        })
