# Generated by Django 5.1.2 on 2024-11-19 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtosservico', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtosservico',
            name='servico',
            field=models.ForeignKey(help_text='Nome do serviço realizado', on_delete=django.db.models.deletion.PROTECT, related_name='servico', to='servicos.servico', verbose_name='Serviço'),
        ),
    ]
