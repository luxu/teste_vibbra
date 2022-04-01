from django.contrib.auth import get_user_model
from django.db import models


class Projeto(models.Model):
    title = models.CharField(
        verbose_name="Título do projeto",
        max_length=50,
        null=False, blank=False
    )
    description = models.CharField(
        verbose_name="Descrição do projeto",
        max_length=50,
        null=True, blank=True
    )
    user = models.ManyToManyField(
        get_user_model(),
    )

    # "title": STRING, "description": STRING, "user_id": ARRAY

    def __str__(self):
        return self.title


class Tempo(models.Model):
    started_at = models.DateTimeField(
        verbose_name="Inicio do Trabalho",
    )
    ended_at = models.DateTimeField(
        verbose_name="Fim do Trabalho",
    )
    projeto = models.ForeignKey(
        Projeto,
        related_name="projetos",
        on_delete=models.CASCADE
    )

    # usuario = models.ForeignKey()

    #  "project_id": INT, "user_id": INT, "started_at": DATETIME, "ended_at": DATETIME,

    def __str__(self):
        return f'{self.started_at}-{self.ended_at}'

# model User "name": STRING, "email": STRING, "login": STRING; "password": STRING }
