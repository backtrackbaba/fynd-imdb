import json

from django.core.management import BaseCommand

from apps.core.models import MovieInfo


def load_data_file() -> json:
    with open('data/imdb.json') as fp:
        return json.load(fp)


def save_to_database(movies: json) -> None:
    print(f"Trying to save {len(movies)} records!")
    movie_info_list = []
    for movie in movies:
        movie_info = MovieInfo()
        movie_info.name = movie.get('name')
        movie_info.director = movie.get('director')
        movie_info.popularity = movie.get('99popularity')
        movie_info.imdb_score = movie.get('imdb_score')
        movie_info.genre = movie.get('genre')

        movie_info_list.append(movie_info)

    MovieInfo.objects.bulk_create(movie_info_list)


class Command(BaseCommand):
    help = 'Seeds database with movie data from the given JSON file'

    def handle(self, *args, **kwargs):
        save_to_database(load_data_file())
