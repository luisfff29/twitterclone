from django.db import models
from twitteruser.models import CustomUser
from tweet.models import TweetMessage


# Create your models here.
class NotificationModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(TweetMessage, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
