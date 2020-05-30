from django.urls import path
from notification import views


urlpatterns = [
    path('', views.notificationview, name='notification'),
]
