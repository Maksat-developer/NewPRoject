from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BboardCreateView.as_view(), name='add'),
    path('api/rubrics/', api_rubrics, name='rubrics'),
    path('api.rubrics/<int:pk>/', api_rubric_detail, name='api_rubric_detail'),



]