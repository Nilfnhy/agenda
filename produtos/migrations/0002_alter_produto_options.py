# Generated by Django 5.1.2 on 2024-11-06 18:00

import django.db.models.functions.text
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': [django.db.models.functions.text.Upper('nome')], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
