# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from royalty.tables import RoyaltyTable
from royalty.models import Royalty
from django_tables2 import RequestConfig

class RoyaltyListView(ListView):
    model = Royalty

    def get_context_data(self, **kwargs):
        context = super(RoyaltyListView, self).get_context_data(**kwargs)
        table = RoyaltyTable(Royalty.objects.all())
        context['royalty'] = RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        return context