from django.contrib.auth.models import User
from django.db import models


class Cell(models.Model):
    cell_value = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return f"cell {self.pk} - value: {self.cell_value}"


class Round(models.Model):
    is_completed = models.BooleanField(default=False)
    jackpot_triggered = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    cell = models.ManyToManyField(
        Cell,
        related_name='rounds',
    )

    def __str__(self):
        return f"round {self.pk}"
