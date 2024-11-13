from django.shortcuts import render
from django.urls import path
from .views import choose_method, start_parsing


urlpatterns = [
	path('', choose_method, name='choose_method'),
	path('start/<str:method>/', start_parsing, name='start_parsing')

]