from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin

from .forms import ServicoModelForm, ProdutosServicoInLine
from .models import Servico


class ServicosView(PermissionRequiredMixin, ListView):
    permission_required = 'servicos.view_servico'
    permission_denied_message = 'Visualizar servico'
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem servicos cadastrados!')

class ServicoAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'servicos.add_servico'
    permission_denied_message = 'Cadastrar servico'
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servicos_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'servico cadastrado com sucesso!'

class ServicoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'servicos.update_servico'
    permission_denied_message = 'Editar servico'
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servicos_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'servico alterado com sucesso!'

class ServicoDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'servicos.delete_servico'
    permission_denied_message = 'Excluir servico'
    model = Servico
    template_name = 'servicos_apagar.html'
    success_url = reverse_lazy('servicos')
    success_message = 'servico excluído com sucesso!'

class ServicoInLineEditView(TemplateResponseMixin, View):
    template_name = 'servico_form_inline.html'

    def get_formset(self, data=None):
        return ProdutosServicoInLine(instance=self.servico, data=data)

    def dispatch(self, request, pk):
        self.servico = get_object_or_404(Servico, id=pk)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'servico': self.servico, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('servicos')
        return self.render_to_response({'servico': self.servico, 'format': formset})