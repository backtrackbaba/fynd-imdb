from rest_framework import serializers

from apps.core.models import MovieInfo


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'
