from django.db import models
from twitteruser.models import CustomUser
from django.utils import timezone


# Create your models here.
class TweetMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    like = models.ManyToManyField(
        CustomUser, related_name="like_tweetmessage_set")

    def __str__(self):
        return self.user.username


class TweetComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(TweetMessage, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
