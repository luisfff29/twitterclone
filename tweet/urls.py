from django.urls import path
from tweet import views


urlpatterns = [
    path('compose/', views.TweetView.as_view(), name='compose'),
    path('<int:id>/', views.TweetDetail.as_view(), name='tweet'),
    path('<int:id>/comment', views.add_comment_to_tweet,
         name='add_comment_to_tweet'),
    path('<int:id>/like', views.add_like, name='add_like'),
    path('<int:id>/dislike', views.remove_like, name='remove_like'),
]
