from django.urls import path 
from .views import index, reviews

urlpatterns = [
    path('',index, name='index'),
    path('reviews/',reviews, name='reviews'),
    

]