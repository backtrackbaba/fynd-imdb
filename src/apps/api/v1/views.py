from rest_framework import viewsets

from apps.api.v1.filters.movies_filter import MoviesFilter
from apps.api.v1.serializers.serializers import MovieSerializer
from apps.core.models import MovieInfo


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.all().order_by('-imdb_score')
    serializer_class = MovieSerializer
    filterset_class = MoviesFilter

    # permission_classes = [permissions.IsAuthenticated]
