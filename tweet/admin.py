from django.contrib import admin
from tweet.models import TweetMessage, TweetComment


# Register your models here.
admin.site.register(TweetMessage)
admin.site.register(TweetComment)
