# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from channels.models import Channel

class ChannelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Channel, ChannelAdmin)
