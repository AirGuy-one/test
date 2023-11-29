from django.contrib import admin
from .models import Cell, Round


class RoundInline(admin.TabularInline):
    model = Round.cell.through
    extra = 1


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    inlines = (RoundInline,)


admin.site.register(Round)
