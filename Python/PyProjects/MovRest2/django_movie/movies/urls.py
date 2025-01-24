from django.urls import path
from .views import MovieDetailView, MovieListView, AddReview

urlpatterns = [
    path('', MovieListView.as_view(), name='movie'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),

]