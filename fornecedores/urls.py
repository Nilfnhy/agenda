from django.urls import path

from .views import FornecedorViews

urlpatterns = [
    path('fornecedores', FornecedorViews.as_view, name='fornecedores'),
]