from django import forms

from .models import Servico

class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do serviço é um campo obrigatório', 'unique': 'Serviço já cadastrado'},
            'descricao': {'required': 'A descrição do serviço é um campo obrigatório'},
            'preco': {'required': 'O preço do servico é um campo obrigatório'},
            }