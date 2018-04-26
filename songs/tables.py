from songs.models import Song
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class SongTable(tables.Table):
    
    class Meta:
        model = Song
        fields = ['title', 'author', 'singer', 'play_time', 'channel', 'royalty']
        sequence = fields