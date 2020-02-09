from django.core.management.base import BaseCommand,CommandError

from menu.models import *
from menu.crawl import crawl_snu

class Command(BaseCommand):
    help = ' '

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        crawl_snu()

