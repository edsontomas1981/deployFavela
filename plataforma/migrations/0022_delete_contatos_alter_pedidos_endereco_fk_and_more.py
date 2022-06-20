# Generated by Django 4.0.4 on 2022-06-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('plataforma', '0021_propostas_previnicio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contatos',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='endereco_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.enderecos'),
        ),
        migrations.AlterField(
            model_name='propostas',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Enderecos',
        ),
    ]
