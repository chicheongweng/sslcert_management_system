# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils import Choices

from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel
from royalty.models import Royalty

class Payee(models.Model):
    TYPE = Choices(_('Company'), _('Person'))
    name = models.CharField(_('name'), max_length=256)
    royalty = models.ForeignKey(Royalty, on_delete=models.CASCADE)
    amount = models.FloatField(_('Amount'), default=0.0)

    class Meta:
        verbose_name = _('Payee')
        verbose_name_plural = _('Payees')