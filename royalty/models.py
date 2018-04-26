# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from channels.models import Channel

class Royalty(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    pay_date = models.DateField(_('Pay Date'))
    amount = models.FloatField(_('Amount'))

    def __unicode__(self):
        return '%s %s' % (self.pay_date, self.amount)

    class Meta:
        verbose_name = _('Royalty')
        verbose_name_plural = _('Royalty')

