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
from django.conf import settings
from payees.models import Payee
from faker import Faker

TOTAL_ROYALTY = 10

names = []
titles = []

loc = 'en_US'
fake=Faker(loc)

for i in range(0,10):
    names.append(Faker(loc).first_name() + ' ' + Faker(loc).last_name())

for i in range(0,50):
    titles.append(Faker(loc).words())

def get_random_first_name(loc='en_US'):
    return Faker(loc).first_name()

def get_random_last_name(loc='en_US'):
    return Faker(loc).last_name()

def get_random_name():
    return random.choice(names)

def get_random_titles():
    return random.choice(titles)

def get_random_words(loc='en_US'):
    return Faker(loc).sentence()

def get_random_sentence(loc='en_US'):
    return Faker(loc).sentence()

def get_random_time_stamp(years=3):
    return str(timezone.now()-timedelta(days=365*randint(0,years)))

def get_random_date(min=1,max=10):
    return str(timezone.now()-timedelta(days=365*randint(min,max))).split(' ')[0]

def get_random_amount(min=100,max=1000):
    return random.randint(min, max)

def get_random_payee_type():
    payee_types = [x[0] for x in settings.PAYEE_TYPES]
    return random.choice(payee_types)

print names
print titles

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

            for payee_type in settings.PAYEE_TYPES:
                name = random.choice(names)
                print "payee_type[1] ", payee_type[1]
                percentage = settings.ROYALTY_PERCENTAGE[payee_type[1]]
                print "percentage ", settings.ROYALTY_PERCENTAGE[payee_type[1]]
                payee = Payee.objects.create(
                    name = name,
                    royalty = royalty,
                    payee_type = payee_type[0],
                    percentage = percentage
                )
                payee.save()


