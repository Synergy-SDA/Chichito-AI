from django.urls import include, path
from .views import UserInformationAPIView

urlpatterns = [
    path('suggest/user_data', UserInformationAPIView.as_view(),name = 'user_data'),
]