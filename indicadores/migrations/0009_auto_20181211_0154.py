# Generated by Django 2.1.2 on 2018-12-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0008_auto_20181125_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pesquisador',
            name='nome',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
