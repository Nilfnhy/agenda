from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

from .forms import FuncionarioModelForm
# Create your views here.

from .models import Funcionario

class FuncionariosView(PermissionRequiredMixin, ListView):
    permission_required = 'funcionarios.view_funcionario'
    permission_denied_message = 'Visualizar funcionario'
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem funcionarios cadastrados!')

class FuncionarioAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'funcionarios.add_funcionario'
    permission_denied_message = 'Cadastrar funcionario'
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário cadastrado com sucesso!'

class FuncionarioUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'funcionarios.update_funcionario'
    permission_denied_message = 'Editar funcionario'
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário alterado com sucesso!'

class FuncionarioDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'funcionarios.delete_funcionario'
    permission_denied_message = 'Excluir funcionario'
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário excluído com sucesso!'