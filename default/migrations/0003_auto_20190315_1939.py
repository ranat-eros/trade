# Generated by Django 2.1.7 on 2019-03-15 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20190315_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='is_active',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='is_active',
            new_name='deleted',
        ),
    ]