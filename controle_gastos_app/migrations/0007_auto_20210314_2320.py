# Generated by Django 3.1.7 on 2021-03-15 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_gastos_app', '0006_auto_20210314_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='valor_gasto',
            field=models.DecimalField(db_column='Valor (R$)', decimal_places=2, default=None, max_digits=10),
        ),
    ]
