# Generated by Django 2.1.7 on 2019-03-15 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_historicalcrypto_historicalcurrency_historicalcurrencyprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalcurrencyprice',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='currencyprice',
            name='unit',
        ),
        migrations.AlterUniqueTogether(
            name='currencyprice',
            unique_together={('crypto', 'currency')},
        ),
    ]
