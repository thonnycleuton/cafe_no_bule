from django import forms
from selectable.forms import AutoCompleteWidget
from .buscalookup import BuscaLookup

from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = '__all__'

    q = forms.CharField(
        label='Search',
        widget=AutoCompleteWidget(BuscaLookup),
        required=False,)
