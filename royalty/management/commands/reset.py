#https://medium.com/@gis10kwo/how-to-create-fake-jobseeker-profiles-using-django-2-0-and-faker-dcfb09bda378

from django.db import models
from django.core.management.base import BaseCommand
from royalty.models import Royalty
from payees.models import Payee

class Command(BaseCommand):

    help = 'reset'

    def handle(self, *args, **options):
        Payee.objects.all().delete()
        Royalty.objects.all().delete()

