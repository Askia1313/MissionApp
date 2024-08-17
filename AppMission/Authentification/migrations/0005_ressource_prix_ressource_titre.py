# Generated by Django 5.0.4 on 2024-08-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0004_remove_tache_predecesseurs_predecesseur'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressource',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ressource',
            name='titre',
            field=models.CharField(default=0.0, max_length=255),
            preserve_default=False,
        ),
    ]
