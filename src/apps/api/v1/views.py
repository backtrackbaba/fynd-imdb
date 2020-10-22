import django_filters
from rest_framework import viewsets, filters

from apps.api.v1.filters.movie_filter import MoviesFilter
from apps.api.v1.permissions.movie_permission import CustomIsAuthenticatedOrReadOnly
from apps.api.v1.serializers.movie_serializer import MovieSerializer
from apps.core.models import MovieInfo


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomIsAuthenticatedOrReadOnly]
    queryset = MovieInfo.objects.all().order_by('-imdb_score')
    serializer_class = MovieSerializer
    filterset_class = MoviesFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
