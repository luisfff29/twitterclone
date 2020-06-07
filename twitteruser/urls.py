from django.urls import path
from twitteruser import views

urlpatterns = [
    path('<str:name>/', views.Profile.as_view(), name='profile'),
    path('<str:name>/follow/', views.follow, name='follow'),
    path('<str:name>/unfollow', views.unfollow, name='unfollow'),
]
