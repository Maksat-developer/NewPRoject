from unicodedata import category
from rest_framework import serializers

from .models import *

class MovieListSerializer(serializers.ModelSerializer):

   class Meta:
        model = Movie
        fields = "__all__"

class MovieCreateSerializer(serializers.ModelSerializer):

   class Meta:
        model = Movie
        fields = ['title', 'tagline', 'descriptions', 'poster', 'year',
        'country', 'url', 'category']


class ActorListSerializer(serializers.ModelSerializer):

   class Meta:
        model = Actor
        fields = "__all__"


class ActorCreateSerializer(serializers.ModelSerializer):

   class Meta:
        model = Actor
        fields = ['name', 'age', 'descriptions', 'image']