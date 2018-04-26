# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils import Choices

from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel
from royalty.models import Royalty
from django.conf import settings

class Payee(models.Model):
    payee_type = models.CharField(_('payee type'), max_length=32, choices=settings.PAYEE_TYPES, default='singer')
    name = models.CharField(_('name'), max_length=256)
    royalty = models.ForeignKey(Royalty, on_delete=models.CASCADE)
    percentage = models.FloatField(_('percentage'), default=0.0)
    amount = models.FloatField(_('amount'), default=0.0)

    def __unicode__(self):
        return '%s, %s, %s' % (self.name, self.payee_type, self.percentage )

    class Meta:
        verbose_name = _('Payee')
        verbose_name_plural = _('Payees')