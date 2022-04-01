from django.contrib import admin

from backend.base.models import Projeto, Tempo


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    ...


@admin.register(Tempo)
class TempoAdmin(admin.ModelAdmin):
    ...
