from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import FornecedorModelForm
from .models import Fornecedor

class FornecedoresViews(ListView):
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresViews, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs

class FornecedorAddView(CreateView):
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')

    class FornecedorDeleteView(DeleteView):
        model = Fornecedor
        template_name = 'fornecedor_apagar.html'
        sucess_url = reverse_lazy('fornecedores')