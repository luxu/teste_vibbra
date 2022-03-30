from django.shortcuts import render

from backend.base.models import Userlist, Item, User


def index(request):
    template_name = 'base/index.html'
    context = {}
    return render(request, template_name, context)


def list_listas(request):
    template_name = 'base/list_listas.html'
    listas = Userlist.objects.all()
    if request.POST.get('enviar'):
        id_lista = int(request.POST.get('id_lista'))
        itens = Item.objects.filter(lists__id=id_lista)
        context = {'itens': itens}
    else:
        context = {
            'listas': listas
        }
    return render(request, template_name, context)


def list_itens(request):
    template_name = 'base/list_itens.html'
    itens = Item.objects.all()
    context = {
        'itens': itens
    }
    return render(request, template_name, context)


def list_users(request):
    template_name = 'base/list_users.html'
    users = User.objects.filter(is_superuser=False)
    context = {
        'users': users
    }
    return render(request, template_name, context)
