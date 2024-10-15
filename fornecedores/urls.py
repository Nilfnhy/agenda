from django.urls import path

from .views import FornecedoresViews, FornecedorAddView

urlpatterns = [
    path('fornecedores', FornecedoresViews.as_view, name='fornecedores'),
    path('fornecedor/adicionar', FornecedorAddView.as_view(), name='fornecedor_adicionar'),
]