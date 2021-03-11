# Generated by Django 3.1.7 on 2021-03-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('B', 'Bar'), ('D', 'Delivery'), ('M', 'Mercado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='estabelecimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estabelecimento', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pagamento', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=10)),
            ],
        ),
    ]