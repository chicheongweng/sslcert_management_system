#https://medium.com/@gis10kwo/how-to-create-fake-jobseeker-profiles-using-django-2-0-and-faker-dcfb09bda378

from django.db import models
from django.core.management.base import BaseCommand
from faker import Faker
import random
import uuid
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from random import randint
from django.contrib.auth.hashers import make_password
from royalty.models import Royalty
from django.utils import timezone

TOTAL_ROYALTY = 100

def get_random_time_stamp(years=3):
    return str(timezone.now()-timedelta(days=365*randint(0,years)))

def get_random_date(min=1,max=10):
    return str(timezone.now()-timedelta(days=365*randint(min,max))).split(' ')[0]

def get_random_amount(min=100,max=1000):
    return random.randint(min, max)

class Command(BaseCommand):

    help = 'generate ' + str(TOTAL_ROYALTY) + ' royalty'

    def handle(self, *args, **options):
        #self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        for _ in range(0, TOTAL_ROYALTY):
            royalty = Royalty.objects.create(
                pay_date=get_random_date(),
                amount=get_random_amount()
            )
            royalty.save()


