# Generated by Django 5.0.4 on 2024-08-04 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0003_tache_predecesseurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tache',
            name='predecesseurs',
        ),
        migrations.CreateModel(
            name='Predecesseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predecesseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='succ_taches', to='Authentification.tache')),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pred_taches', to='Authentification.tache')),
            ],
            options={
                'unique_together': {('tache', 'predecesseur')},
            },
        ),
    ]
