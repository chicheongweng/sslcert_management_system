# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from royalty.models import Royalty

class RoyaltyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Royalty, RoyaltyAdmin)