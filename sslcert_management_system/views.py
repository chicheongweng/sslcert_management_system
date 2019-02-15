from payees.models import Payee
from royalty.models import Royalty
from songs.models import Song
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['num_royalty'] = Royalty.objects.count()
        context['num_songs'] = Song.objects.count()
        context['num_payees'] = Payee.objects.count()
        return context