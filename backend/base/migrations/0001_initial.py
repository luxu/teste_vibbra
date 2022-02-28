# Generated by Django 4.0.2 on 2022-02-28 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(choices=[(True, 'Ativa'), (False, 'Inativa')], default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_usuary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(choices=[(True, 'Ativa'), (False, 'Inativa')], default=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome da lista')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_list', to='base.usuary')),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listas',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(choices=[(True, 'Ativa'), (False, 'Inativa')], default=True)),
                ('description', models.CharField(max_length=50, verbose_name='Descrição do Item')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_item', to='base.item')),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='base.lists')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
    ]