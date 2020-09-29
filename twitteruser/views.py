from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from notification.models import NotificationModel
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from twitteruser.helpers import random_users


class Index(LoginRequiredMixin, View):
    def get(self, request):
        current_user = CustomUser.objects.get(username=request.user.username)
        users_following = current_user.following.all()
        all_tweets = TweetMessage.objects.filter(user__in=users_following).order_by(
            '-date') | TweetMessage.objects.filter(user=current_user).order_by(
                '-date')
        tweets = TweetMessage.objects.filter(user=current_user)
        num_notif = NotificationModel.objects.filter(
            user=request.user, viewed=False).count()
        return render(request, 'twitteruser/index.html', {
            'all_tweets': all_tweets,
            'who_to_follow': random_users(request.user.username),
            'tweets': tweets,
            'num_notif': num_notif
        })


class Profile(View):
    def get(self, request, name):
        usuario = CustomUser.objects.get(username=name)
        tweets = TweetMessage.objects.filter(user=usuario).order_by('-date')
        try:
            current_user = CustomUser.objects.get(
                username=request.user.username)
            users_following = current_user.following.all()
            following = usuario in users_following
            num_notif = NotificationModel.objects.filter(
                user=request.user, viewed=False).count()
        except CustomUser.DoesNotExist:
            following = False
            num_notif = 0

        return render(request, 'twitteruser/profile.html', {
            'tweets': tweets,
            'profile_user': usuario,
            'following': following,
            'num_notif': num_notif
        })


@login_required
def follow(request, name):
    if request.user.username == name:
        return HttpResponseRedirect(reverse('profile', args=(name,)))

    follow_user = CustomUser.objects.get(username=name)
    current_user = CustomUser.objects.get(username=request.user.username)
    current_user.following.add(follow_user)
    return HttpResponseRedirect(reverse('profile', args=(name,)))


@login_required
def unfollow(request, name):
    if request.user.username == name:
        return HttpResponseRedirect(reverse('profile', args=(name,)))

    unfollow_user = CustomUser.objects.get(username=name)
    current_user = CustomUser.objects.get(username=request.user.username)
    current_user.following.remove(unfollow_user)
    return HttpResponseRedirect(reverse('profile', args=(name,)))
