from django.urls import path

from .views import UserInformationAPIView

urlpatterns = [
    path('suggest/', UserInformationAPIView.as_view(), name='user-info'),
]