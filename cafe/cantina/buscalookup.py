from selectable.base import ModelLookup
from selectable.registry import registry
from .models import Solicitacao


class BuscaLookup(ModelLookup):
    model = Solicitacao
    search_fields = ('text__icontains', )


registry.register(BuscaLookup)
