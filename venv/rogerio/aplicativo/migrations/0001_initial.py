# Generated by Django 5.0.6 on 2024-05-08 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('casado', models.BooleanField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
