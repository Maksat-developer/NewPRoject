from django.urls import path
from .views import index, by_rubric, BbCreateViews, BbDeleteViews

urlpatterns = [
    path('add/', BbCreateViews.as_view(), name='add'),
    path('delete/<int:pk>/', BbDeleteViews.as_view(), name='delete'),
    path('bboard/', index, name='index'),
    path('bboard/<int:rubric_id>/',by_rubric, name='by_rubric'),


]