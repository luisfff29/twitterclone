from django.urls import path
from authentication import views


urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('signup/', views.signupview, name='signup'),
]
