from django.urls import path
from authentication import views


urlpatterns = [
    path('', views.AuthHomeView.as_view(), name='auth_home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]