# Generated by Django 2.2.5 on 2019-10-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0015_auto_20191008_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='campoindicador',
            name='nome_variavel',
            field=models.CharField(default='', max_length=500),
        ),
    ]