# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Channel(models.Model):
    name = models.CharField(_('Name'), max_length=256)

    def __unicode__(self):
        return '%s' % (self.name)