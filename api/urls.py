from django.contrib import admin
from django.urls import path, include

from backend.views import TestApi


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestApi.as_view(), name='api'),
]
