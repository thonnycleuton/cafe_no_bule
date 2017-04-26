from cafe.cantina.views import SolicitacaoView, SolicitacaoCreate, SolicitacaoUpdate, SolicitacaoDelete
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^$', SolicitacaoView.as_view(), name='read'),
                       url(r'^criar/$', SolicitacaoCreate.as_view(), name='create'),
                       url(r'^editar/(?P<pk>\d+)/$', SolicitacaoUpdate.as_view(), name='edit'),
                       url(r'^excluir/(?P<pk>\d+)/$', SolicitacaoDelete.as_view(), name='delete'),
                       )
