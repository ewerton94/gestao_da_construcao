# Generated by Django 2.2.5 on 2019-10-19 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0017_auto_20191008_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicador',
            options={'ordering': ['ordem', 'id']},
        ),
        migrations.DeleteModel(
            name='Resultado',
        ),
    ]
