# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from songs.models import Song
from songs.tables import SongTable
from django_tables2 import RequestConfig

class SongListView(ListView):
    model = Song

    def get_context_data(self, **kwargs):
        context = super(SongListView, self).get_context_data(**kwargs)
        context['songs'] = SongTable(Song.objects.all())
        return context