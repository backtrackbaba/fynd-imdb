import django_filters
from rest_framework import viewsets, filters

from apps.api.v1.filters.movies_filter import MoviesFilter
from apps.api.v1.serializers.serializers import MovieSerializer
from apps.core.models import MovieInfo


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.all().order_by('-imdb_score')
    serializer_class = MovieSerializer
    filterset_class = MoviesFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    # permission_classes = [permissions.IsAuthenticated]
