# Generated by Django 2.2.4 on 2020-03-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0024_empreendimento_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]