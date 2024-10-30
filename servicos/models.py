from django.db import models

import fornecedores.models
from produtosservico.models import ProdutosServico


class Servico(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome completo do servico', unique='True')
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, help_text='Preço do servico')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observações do serviço')
    produto = models.ManyToManyField('produtos.Produto', through='produtosservico.ProdutosServico')

    @property
    def produtos(self):
        return ProdutosServico.objects.filter(servico=self)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.nome
