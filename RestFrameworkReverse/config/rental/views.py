from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


class FriendModelViewSet(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer

class BelongingModelViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


class BorrowedModelViewSet(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerialiser
