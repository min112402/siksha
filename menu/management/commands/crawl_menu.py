from django.core.management.base import BaseCommand,CommandError

from menu.models import *
from menu.crawl import crawl_snu, crawl_snuco, crawl_dorm

class Command(BaseCommand):
    help = ' '

    def add_arguments(self, parser):
        parser.add_argument('--dorm', action="store_true")
        parser.add_argument('--snuco', action="store_true")

    def handle(self, *args, **options):
        if options['dorm']:
            crawl_dorm()
            return
        if options['snuco']:
            crawl_snuco()
            return
        crawl_snu()
        self.stdout.write(self.style.SUCCESS('Success'))
