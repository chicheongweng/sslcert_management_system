from royalty.models import Royalty
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class RoyaltyTable(tables.Table):
    #price = ColumnWithThousandsSeparator()
    
    class Meta:
        model = Royalty
        fields = ['id', 'amount', 'pay_date']
        sequence = ['id', 'amount', 'pay_date']
        #fields = ['time_stamp', 'order_type', 'symbol', 'price']
        #sequence = ['time_stamp', 'order_type', 'symbol', 'price']
