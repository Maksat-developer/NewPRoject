from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializer import UserSerializer, GroupSerializer, CategorySerializer,SubCategorySerializer, AnnouncementSerializers
from .models import Category, SubCategories, Announcement


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryLiatAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryLiatAPIView(generics.ListAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategorySerializer


class AnnouncementLiatAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all().order_by('-data_published')
    serializer_class = AnnouncementSerializers



def index(request):
    return render(request, "mysite/index.html")
