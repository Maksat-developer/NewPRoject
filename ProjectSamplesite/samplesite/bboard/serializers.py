from rest_framework import serializers
from .models import Rubric, Bboard



class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = ('id', 'name')




class BboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bboard
        fields = ('id', 'title', 'content', 'price', 'rubric', 'published')


    