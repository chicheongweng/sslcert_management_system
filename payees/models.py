# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils import Choices

from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel
from royalty.models import Royalty

PAYEE_TYPES = (
    ('singer', 'Singer'),
    ('author', 'Author'),
    ('company', 'Company')
)

class Payee(models.Model):
    TYPE = Choices(_('Company'), _('Singer'), _('Author'))
    payee_type = models.CharField(_('payee type'), max_length=32, choices=PAYEE_TYPES, default='singer')
    name = models.CharField(_('name'), max_length=256)
    royalty = models.ForeignKey(Royalty, on_delete=models.CASCADE)
    percentage = models.FloatField(_('percentage'), default=0.0)

    class Meta:
        verbose_name = _('Payee')
        verbose_name_plural = _('Payees')