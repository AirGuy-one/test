from django.shortcuts import render
from .models import Round, Cell
import random


def main(request):
    if request.method == 'POST':
        user = request.user

        current_round = Round.objects.filter(user=user).order_by('-pk').first()
        if current_round and current_round.jackpot_triggered:
            Round.objects.create(user=user)
            return render(request, 'index.html', context={'cell': 'To play game press the button'})

        if not current_round:
            current_round = Round.objects.create(user=user)

        excluded_cells = current_round.cell.all()
        available_cells = Cell.objects.exclude(pk__in=excluded_cells)

        if available_cells.exists():
            weights = available_cells.values_list('weight', flat=True)
            chosen_cell = random.choices(available_cells, weights, k=1).pop()

            current_round.cell.add(chosen_cell)
            return render(request, 'index.html', context={'cell': chosen_cell.cell_value})
        else:
            current_round.jackpot_triggered = True
            current_round.is_completed = True
            current_round.save()
            return render(request, 'index.html', context={'cell': 'Jackpot!'})

    return render(request, 'index.html', context={'cell': 'To play game press the button'})
