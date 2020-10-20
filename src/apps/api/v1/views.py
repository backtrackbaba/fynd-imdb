from rest_framework import viewsets

from apps.core.models import MovieInfo
from apps.core.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MovieInfo.objects.all().order_by('-imdb_score')
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticated]
