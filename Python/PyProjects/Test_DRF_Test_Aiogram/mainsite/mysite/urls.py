
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'movie', views.UserViewSet)


urlpatterns = [
                path("", views.index, name="main"),
                path("api/v1/user/", views.UserViewSet.as_view({'get': 'list'})),
                path("api/v1/cat_list/", views.CategoryLiatAPIView.as_view()),
                path("api/v1/sub_cat_list/", views.SubCategoryLiatAPIView.as_view()),
                path("api/v1/obj_list/", views.AnnouncementLiatAPIView.as_view()),

]
