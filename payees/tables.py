from payees.models import Payee
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class PayeeTable(tables.Table):
    #price = ColumnWithThousandsSeparator()
    
    class Meta:
        model = Payee
        fields = ['name', 'payee_type', 'percentage', 'amount', 'royalty']
        sequence = fields
        #sequence = ['time_stamp', 'order_type', 'symbol', 'price']
