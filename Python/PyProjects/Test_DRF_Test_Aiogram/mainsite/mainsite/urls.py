
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mysite.views import *
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns_yasg



router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include("mysite.urls")),
                path('router/', include(router.urls)),
                path('auth/', include('djoser.urls')),
                path('api-auth/', include('rest_framework.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += urlpatterns_yasg
