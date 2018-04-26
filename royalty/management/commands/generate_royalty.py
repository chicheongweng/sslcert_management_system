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
from songs.models import Song
from faker import Faker
from channels.models import Channel

TOTAL_SONGS = 30
TOTAL_ROYALTY = TOTAL_SONGS

names = []
titles = []

loc = 'en_US'
fake=Faker(loc)

for i in range(0,10):
    names.append(Faker(loc).first_name() + ' ' + Faker(loc).last_name())

for i in range(0,50):
    titles.append(Faker(loc).sentence())

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

def get_random_channel():
    number_of_channels = Channel.objects.count() - 1
    random_index = int(random.random()*number_of_channels)+1
    random_channel = Channel.objects.get(pk = random_index)
    return random_channel

def create_song():
    title = random.choice(titles)
    author = random.choice(names)
    singer = random.choice(names)
    play_time = fake.date_time_between(start_date='-10y', end_date='now')
    channel=get_random_channel()
    return {
            'title': title,
            'author': author,
            'singer': singer,
            'play_time': play_time,
            'channel': channel
            }

class Command(BaseCommand):

    help = 'generate ' + str(TOTAL_ROYALTY) + ' royalty'

    def handle(self, *args, **options):
        #self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        for _ in range(0, TOTAL_SONGS):

            s = create_song()

            pay_date = get_random_date()
            amount=get_random_amount()

            royalty = Royalty.objects.create(
                pay_date=pay_date,
                amount=amount
            )
            royalty.save()

            song = Song.objects.create(
                title = s['title'],
                singer = s['singer'],
                author = s['author'],
                play_time = s['play_time'],
                channel = s['channel'],
                royalty = royalty
            )
            song.save()

            percentage = settings.ROYALTY_PERCENTAGE['singer']
            singer = Payee.objects.create(
                name = song.singer,
                royalty = royalty,
                payee_type = 'singer',
                percentage = percentage,
                amount = royalty.amount * percentage
            )
            singer.save()

            percentage = settings.ROYALTY_PERCENTAGE['author']
            author = Payee.objects.create(
                name = song.author,
                royalty = royalty,
                payee_type = 'author',
                percentage = percentage,
                amount = royalty.amount * percentage
            )
            author.save()

            percentage = settings.ROYALTY_PERCENTAGE['company']
            company = Payee.objects.create(
                name = song.author,
                royalty = royalty,
                payee_type = 'company',
                percentage = percentage,
                amount = royalty.amount * percentage
            )
            company.save()


