from twitteruser.models import CustomUser
import random


def random_users(username):
    all_users = CustomUser.objects.exclude(username=username)
    list_users = list(all_users)
    random.shuffle(list_users)
    return list_users
