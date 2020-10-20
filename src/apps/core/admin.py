from django.contrib import admin

from apps.core.models import MovieInfo


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity', 'imdb_score')


admin.site.register(MovieInfo, MovieAdmin)
