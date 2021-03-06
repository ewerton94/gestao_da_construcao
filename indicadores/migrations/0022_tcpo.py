# Generated by Django 2.2.5 on 2019-10-27 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0021_resultado_calculado'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCPO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcpos', to='indicadores.Indicador')),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.Referencia')),
            ],
        ),
    ]
