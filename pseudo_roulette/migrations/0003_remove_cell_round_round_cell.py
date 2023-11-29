# Generated by Django 4.2.7 on 2023-11-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudo_roulette', '0002_remove_round_cell_cell_round'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cell',
            name='round',
        ),
        migrations.AddField(
            model_name='round',
            name='cell',
            field=models.ManyToManyField(related_name='rounds', to='pseudo_roulette.cell'),
        ),
    ]
