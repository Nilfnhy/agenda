from django.views.generic import ListView

from .models import Fornecedor

class FornecedorViews(ListView):
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedorViews, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs