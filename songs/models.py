# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Song(models.Model):
    title = models.CharField(_('Name'), max_length=256)
    author = models.CharField(_('Author'), max_length=256)
    singer = models.CharField(_('Singer'), max_length=256)
    class Meta:
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')