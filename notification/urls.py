from django.urls import path
from notification import views


urlpatterns = [
    path('', views.NotificationView.as_view(), name='notification'),
]
