from django.contrib import admin

from agendamentos.models import Agendamento


# Register your models here.

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente', 'funcionario', 'valor')
    search_fields = ('ciente', 'funcionario')
    list_filter = ('ciente', 'servico')