from django.contrib.auth.models import User
from django.db import models

from backend import settings
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


class Userlist(Base):
    title = models.CharField(
        'Nome da lista',
        max_length=50
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_list',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'


class Item(Base):
    title = models.CharField(
        'Título',
        max_length=50
    )
    description = models.CharField(
        'Descrição',
        max_length=50
    )
    userlist = models.ForeignKey(
        Userlist,
        related_name='lists',
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        related_name='sub_itens',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
