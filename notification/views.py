from django.shortcuts import render
from notification.models import NotificationModel


# Create your views here.
def notificationview(request):
    return render(request, 'notification/notification.html')
