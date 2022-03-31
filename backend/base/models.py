from django.db import models

from backend.base import constants


class Base(models.Model):
    """ Base parent model for all the models """
    created_at = models.DateTimeField("Criado em", auto_now_add=True, null=True)
    modified_at = models.DateTimeField("Atualizado em", auto_now=True, null=True)
    status = models.BooleanField(choices=constants.STATUS, default=constants.ATIVO)

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True


class Projeto(Base):
    description = models.CharField(
        "Descrição",
        max_length=50
    )

    def __str__(self):
        return self.description


class Tempo(Base):
    title = models.CharField(
        'Título',
        max_length=50
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
