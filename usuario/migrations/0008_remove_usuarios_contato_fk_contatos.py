# Generated by Django 4.0.4 on 2022-06-11 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_usuarios_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='contato_fk',
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
                ('contato', models.CharField(max_length=50)),
                ('usuario_fk', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
