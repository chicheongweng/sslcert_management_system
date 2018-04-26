# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from songs.models import Song

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Song, SongAdmin)