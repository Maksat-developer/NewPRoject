


from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Movie, Actor

from rest_framework import viewsets

from .serializres import MovieListSerializer, ActorListSerializer, MovieCreateSerializer, ActorCreateSerializer



# class MovieListView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieListSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['year', 'country']
#     search_fields = ['title', 'genres']
#     permission_classes = [IsAuthenticated]

class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['year', 'country']
    search_fields = ['title', 'genres']
    permission_classes = [IsAuthenticated]

# class MovieViewSets(ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieListSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filter_fields = ['year']
#     search_fields = ['title']
#     ordering_fields = ['country', 'genres']
#     permission_classes = [IsAuthenticated]


# class MovieCreateView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class= MovieCreateSerializer


# class MovieDeteilView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieListSerializer



# class ActorListView(generics.ListAPIView):

#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer



# class ActorCreateView(generics.ListCreateAPIView):

#     queryset = Actor.objects.all()
#     serializer_class = ActorCreateSerializer

   

# class ActorDeteilView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer


    




