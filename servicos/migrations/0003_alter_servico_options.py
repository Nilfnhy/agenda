# Generated by Django 5.1.2 on 2024-11-06 18:00

import django.db.models.functions.text
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_servico_produto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': [django.db.models.functions.text.Upper('nome')], 'verbose_name': 'Servico', 'verbose_name_plural': 'Servicos'},
        ),
    ]