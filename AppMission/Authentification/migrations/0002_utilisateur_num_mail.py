# Generated by Django 3.2.12 on 2024-08-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='num_mail',
            field=models.IntegerField(default=0),
        ),
    ]
