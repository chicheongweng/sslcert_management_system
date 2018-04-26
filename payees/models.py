# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils import Choices

from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel

class Payee(models.Model):
    TYPE = Choices(_('Company'), _('Person'))
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('Payee')
        verbose_name_plural = _('Payees')