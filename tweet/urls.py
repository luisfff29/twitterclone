from django.urls import path
from tweet import views


urlpatterns = [
    path('compose/', views.tweetview, name='compose'),
    path('<int:id>/', views.tweetdetail, name='tweet'),
]
