from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import FornecedorModelForm
from .models import Fornecedor

class FornecedoresViews(PermissionRequiredMixin, ListView):
    permission_required = 'fornecedores.view_fornecedor'
    permission_denied_message = 'Visualizar fornecedor'
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresViews, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count()>0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem fornecedores cadastrados!')

class FornecedorAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'fornecedores.add_fornecedor'
    permission_denied_message = 'Cadastrar fornecedor'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor cadastrado com sucesso!'

class FornecedorUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'fornecedores.update_fornecedor'
    permission_denied_message = 'Editar fornecedor'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor alterado com sucesso!'

class FornecedorDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'fornecedores.delete_fornecedor'
    permission_denied_message = 'Excluir fornecedor'
    model = Fornecedor
    template_name = 'fornecedor_apagar.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor apagado com sucesso!'