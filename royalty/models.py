# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils import Choices

from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel

class Royalty(models.Model):
    created_at = models.DateTimeField(_('Created At'))
    pay_date = models.DateField(_('Pay Date'))
    amount = models.FloatField(_('Amount'))

    class Meta:
        verbose_name = _('Royalty')
        verbose_name_plural = _('Royalty')