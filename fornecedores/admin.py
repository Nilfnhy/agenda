from django.contrib import admin

from fornecedores.models import Fornecedor


# Register your models here.

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'fone')
    search_fields = ('nome', 'fone')