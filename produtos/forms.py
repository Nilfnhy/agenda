from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do produto é um campo obrigatório'},
            'preco': {'required': 'O preço do produto é um campo obrigatório'},
            'quantidade': {'required': 'A quantidade do produto é um campo obrigatório'},
            }