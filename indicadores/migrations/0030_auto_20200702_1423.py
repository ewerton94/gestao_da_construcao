# Generated by Django 2.2 on 2020-07-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0029_auto_20200702_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='logenvioderesultado',
            name='sucesso',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regitroerrosenvios',
            name='codigo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
