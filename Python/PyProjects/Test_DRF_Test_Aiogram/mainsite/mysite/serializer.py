from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, SubCategories, Announcement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'



class AnnouncementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'