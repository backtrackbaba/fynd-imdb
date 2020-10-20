from django_filters import rest_framework as filters

from apps.core.models import MovieInfo


class CharArrayFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass


class MoviesFilter(filters.FilterSet):
    popularity__gte = filters.NumberFilter(field_name="popularity", lookup_expr='gte')
    popularity__gt = filters.NumberFilter(field_name="popularity", lookup_expr='gt')
    popularity__lte = filters.NumberFilter(field_name="popularity", lookup_expr='lte')
    popularity__lt = filters.NumberFilter(field_name="popularity", lookup_expr='lt')

    score__gte = filters.NumberFilter(field_name="imdb_score", lookup_expr='gte')
    score__gt = filters.NumberFilter(field_name="imdb_score", lookup_expr='gt')
    score__lte = filters.NumberFilter(field_name="imdb_score", lookup_expr='lte')
    score__lt = filters.NumberFilter(field_name="imdb_score", lookup_expr='lt')

    genre__contains = CharArrayFilter(field_name='genres', lookup_expr='contains')

    class Meta:
        model = MovieInfo
        fields = ['genre__contains']
