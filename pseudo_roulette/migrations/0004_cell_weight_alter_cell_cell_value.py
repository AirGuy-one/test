# Generated by Django 4.2.7 on 2023-11-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudo_roulette', '0003_remove_cell_round_round_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='weight',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cell',
            name='cell_value',
            field=models.PositiveIntegerField(),
        ),
    ]