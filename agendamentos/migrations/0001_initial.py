# Generated by Django 5.1.2 on 2024-10-30 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('funcionarios', '0002_rename_data_admissão_funcionario_data_admissao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(help_text='Data e hora do agendamento', unique=True, verbose_name='Horário')),
                ('cliente', models.ForeignKey(help_text='Cliente que agendou', on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente', verbose_name='Cliente')),
                ('funcionario', models.ForeignKey(help_text='Nome do funcionário', on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario', verbose_name='Funcionário')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]