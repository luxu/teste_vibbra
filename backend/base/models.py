from django.contrib.auth.models import User
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


class Usuary(Base):
    user = models.OneToOneField(
        User,
        related_name='user_usuary',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Lists(Base):
    name = models.CharField(
        'Nome da lista',
        max_length=50
    )
    user = models.ForeignKey(
        Usuary,
        on_delete=models.CASCADE,
        related_name='user_list',
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'


class Item(Base):
    description = models.CharField(
        'Descrição do Item',
        max_length=50
    )
    lists = models.ForeignKey(
        Lists,
        related_name='lists',
        on_delete=models.CASCADE,
    )
    father = models.ForeignKey(
        'self',
        related_name='father_item',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
