import random

from django.core.management import BaseCommand

BASE_URL = "https://fynd.saiprasad.io/api/v1/movies/{num}/?format=json"
URL_FILE = 'urls.txt'
LIMIT = 1000
RECORDS = 248


class Command(BaseCommand):
    """
    Command to help generate random URL's to test.

    Can be extended further to also randomly include filter parameters.
    """
    help = "Command to help generate random URL's to test."

    def handle(self, *args, **options):
        with open(URL_FILE, 'w') as fp:
            for iteration in range(1, LIMIT):
                fp.write(BASE_URL.replace('{num}', str(random.randint(1, RECORDS))) + '\n')
