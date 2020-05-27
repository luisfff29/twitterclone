from django.urls import path
from twitteruser import views

urlpatterns = [
    path('<str:name>', views.profile, name='profile'),
]
