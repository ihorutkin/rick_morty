import time

from django.core.management import BaseCommand
from django.db import connections
from psycopg2 import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs) -> None:
        self.stdout.write("Watching for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
