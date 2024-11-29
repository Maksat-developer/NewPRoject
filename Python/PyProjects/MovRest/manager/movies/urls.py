from django.urls import path

from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'movie', views.MovieViewSets)



urlpatterns = [
    path("api/v1/movie-list/", views.MovieViewSets.as_view({'get': 'list'})),
    path("api/v1/deteil-mov/<int:pk>/", views.MovieViewSets.as_view({'put': 'update'})),
    
    # path("api/v1/create-mov/", views.MovieCreateView.as_view()),
    

    # path("api/v1/actors-list/", views.ActorListView.as_view()),
    # path("api/v1/create-ac/", views.ActorCreateView.as_view()),
    # path("api/v1/deteil-ac/<int:pk>/", views.ActorDeteilView.as_view()),
]

