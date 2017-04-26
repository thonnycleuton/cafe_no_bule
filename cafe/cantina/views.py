from django.contrib import messages

from cafe.cantina.form import SolicitacaoForm
from cafe.cantina.models import Solicitacao
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class SolicitacaoCreate(CreateView):
    model = Solicitacao
    template_name = 'cantina/form.html'
    fields = "__all__"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Salvo com sucesso!'))
        return redirect('solicitacoes:read')


class SolicitacaoView(ListView):
    template_name = 'cantina/list.html'
    model = Solicitacao
    paginate_by = 100

    def get(self, request, **kwargs):
        self.object_list = self.get_queryset()
        if 'q' in request.GET:
            self.object_list = self.object_list.filter(text__icontains=request.GET.get('q'))

        context = super(SolicitacaoView, self).get_context_data(**kwargs)
        context['search'] = SolicitacaoForm()

        return self.render_to_response(context)


class SolicitacaoDelete(DeleteView):
    model = Solicitacao
    success_url = '/'
    template_name = 'cantina/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.error(self.request, ('Deletado com sucesso!'))
        return HttpResponseRedirect(success_url)


class SolicitacaoUpdate(UpdateView):
    model = Solicitacao
    template_name = 'cantina/form.html'
    fields = "__all__"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Alterado com sucesso!'))
        return redirect('solicitacoes:read')
