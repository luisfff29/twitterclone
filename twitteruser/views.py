from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import TweetMessage
from twitteruser.models import CustomUser
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def index(request):
    tweets = TweetMessage.objects.all().order_by('-date')
    return render(request, 'twitteruser/index.html', {'tweets': tweets})


@login_required
def profile(request, name):
    usuario = CustomUser.objects.get(username=name)
    tweets = TweetMessage.objects.filter(user=usuario).order_by('-date')
    current_user = CustomUser.objects.get(username=request.user.username)
    boolean = usuario in current_user.following.all()
    num_tweets = tweets.count()
    num_follow = usuario.following.count()
    return render(request, 'twitteruser/profile.html', {
        'tweets': tweets,
        'profile_user': usuario,
        'boolean': boolean,
        'num_tweets': num_tweets,
        'num_follow': num_follow
    })


def follow(request, name):
    if request.user.username == name:
        return HttpResponseRedirect(reverse('profile', args=(name,)))

    follow_user = CustomUser.objects.get(username=name)
    current_user = CustomUser.objects.get(username=request.user.username)
    current_user.following.add(follow_user)
    return HttpResponseRedirect(reverse('profile', args=(name,)))


def unfollow(request, name):
    if request.user.username == name:
        return HttpResponseRedirect(reverse('profile', args=(name,)))

    unfollow_user = CustomUser.objects.get(username=name)
    current_user = CustomUser.objects.get(username=request.user.username)
    current_user.following.remove(unfollow_user)
    return HttpResponseRedirect(reverse('profile', args=(name,)))
