# Generated by Django 2.2.5 on 2019-11-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0022_tcpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencia',
            name='situacao',
            field=models.BooleanField(default=True),
        ),
    ]