from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ai.urls')),  # Include the ai app URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]