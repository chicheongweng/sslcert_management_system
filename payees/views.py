# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from payees.models import Payee
from payees.tables import PayeeTable
from django_tables2 import RequestConfig

class PayeeListView(ListView):
    model = Payee

    def get_context_data(self, **kwargs):
        context = super(PayeeListView, self).get_context_data(**kwargs) 
        context['payees'] = PayeeTable(Payee.objects.all())
        return context