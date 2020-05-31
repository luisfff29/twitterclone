from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from notification.models import NotificationModel
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def index(request):
    usuario = CustomUser.objects.get(username=request.user.username)
    followed = usuario.following.all()
    tweets = TweetMessage.objects.filter(user__in=followed).order_by(
        '-date') | TweetMessage.objects.filter(user=usuario).order_by('-date')
    mytweets = TweetMessage.objects.filter(user=usuario).count()
    num_notif = NotificationModel.objects.filter(
        user=request.user, viewed=False).count()
    return render(request, 'twitteruser/index.html', {
        'tweets': tweets,
        'num_tweets': mytweets,
        'num_notif': num_notif
    })


def profile(request, name):
    usuario = CustomUser.objects.get(username=name)
    tweets = TweetMessage.objects.filter(user=usuario).order_by('-date')
    try:
        current_user = CustomUser.objects.get(username=request.user.username)
        boolean = usuario in current_user.following.all()
        num_notif = NotificationModel.objects.filter(
            user=request.user, viewed=False).count()
    except CustomUser.DoesNotExist:
        boolean = False
        num_notif = 0
    num_tweets = tweets.count()
    return render(request, 'twitteruser/profile.html', {
        'tweets': tweets,
        'profile_user': usuario,
        'boolean': boolean,
        'num_tweets': num_tweets,
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
