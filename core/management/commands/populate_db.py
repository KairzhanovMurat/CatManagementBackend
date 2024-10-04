from django.core.management import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('populating database with data...')
        try:
            ...
        except:
            self.stdout.write(self.style.ERROR('error populating db'))
        self.stdout.write(self.style.SUCCESS('successfully populated db'))
