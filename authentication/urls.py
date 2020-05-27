from django.urls import path
from authentication import views


urlpatterns = [
    path('login/', views.loginview),
    path('signup/', views.signupview),
]
