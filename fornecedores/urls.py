from django.urls import path

from .views import FornecedoresViews, FornecedorAddView, FornecedorUpdateView, FornecedorDeleteView

urlpatterns = [
    path('fornecedores', FornecedoresViews.as_view, name='fornecedores'),
    path('fornecedor/adicionar', FornecedorAddView.as_view(), name='fornecedor_adicionar'),
    path('<int:pk>/fornecedor/editar/', FornecedorUpdateView.as_view(), name='fornecedor_editar'),
    path('<int:pk>/fornecedor/apagar/', FornecedorDeleteView.as_view(), name='fornecedor_deletar'),
]