from django.contrib import admin
from django.urls import path, include
from .api import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),


]
