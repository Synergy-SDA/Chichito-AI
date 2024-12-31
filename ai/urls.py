from django.urls import path

from .views import UserInformationAPIView

urlpatterns = [
    path('user-info/', UserInformationAPIView.as_view(), name='user-info'),
]