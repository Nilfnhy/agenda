from django.db import models

import fornecedores.models
from ordemservicos.models import OrdemServicos


class Agendamento(models.Model):
    horario = models.DateTimeField('Horário', help_text='Data e hora do agendamento', unique=True)
    cliente = models.ForeignKey('clientes.Cliente', verbose_name='Cliente', help_text='Cliente que agendou', on_delete=models.PROTECT)
    funcionario = models.ForeignKey('funcionarios.Funcionario', verbose_name='Funcionário',  help_text='Nome do funcionário',
                                    on_delete=models.PROTECT)
    servico = models.ManyToManyField('servicos.Servico', verbose_name='Serviço', through='ordemservicos.OrdemServicos')

    @property
    def servicos(self):
        return OrdemServicos.objects.filter(agendamento=self)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'Cliente: {self.cliente}'
