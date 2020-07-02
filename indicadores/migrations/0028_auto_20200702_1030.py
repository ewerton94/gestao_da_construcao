# Generated by Django 2.2 on 2020-07-02 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0027_auto_20200307_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='codigo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resultadocalculado',
            name='codigo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='LogEnvioDeResultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dados_iniciais', models.TextField(default='')),
                ('indicadores', models.TextField(default='')),
                ('codigo', models.CharField(blank=True, max_length=500, null=True)),
                ('conferido_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.Cliente')),
                ('empreendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.Empreendimento')),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.Referencia')),
            ],
        ),
    ]
