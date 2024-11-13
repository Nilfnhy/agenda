from django.contrib import admin

from produtos.models import Produto
from produtosservico.models import ProdutosServico

from servicos.models import Servico


# Register your models here.

class ProdutosServicoInline(admin.TabularInline):
    model = ProdutosServico
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'get_produtos')
    inlines = [ProdutosServicoInline]
    search_fields = ('nome', 'descricao')

    def get_produtos(self, obj):
        return ', '.join([prd.nome for prd in Produto.objects.filter(servico=obj.id)])

    get_produtos.short_description = 'Produtos utilizados'