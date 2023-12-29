from django.contrib.admin import register, ModelAdmin

from pypro.turmas.models import Turma


@register(Turma)
class TurmaAdmin(ModelAdmin):
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
