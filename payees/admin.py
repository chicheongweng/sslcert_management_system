# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from payees.models import Payee

class PayeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Payee, PayeeAdmin)