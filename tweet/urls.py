from django.urls import path
from tweet import views


urlpatterns = [
    path('compose/', views.TweetView.as_view(), name='compose'),
    path('<int:id>/', views.TweetDetail.as_view(), name='tweet'),
    path('<int:id>/comment', views.add_comment_to_tweet,
         name='add_comment_to_tweet'),
]
