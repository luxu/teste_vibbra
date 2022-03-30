from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.base.models import Userlist, Item
from .serializer import (
    ListsManagementListSerializer,
    UsersManagementListSerializer,
    ItensManagementListSerializer,
    UserCreateSerializer,
    UserSerializer,
    ListCreateSerializer
)


@api_view(["GET"])
def users_list(request, pk):
    """Listar os usuários"""
    try:
        serializer = UsersManagementListSerializer(
            user_id=pk
        )
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return Response(
            f"Não existe Usuário com ID..{pk}",
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def user_create(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def user_update(request, user_id=None):
    # if not self.user_has_permission():
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    if user_id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(id=user_id)
    serializer_class = UserSerializer(
        user, data=request.data, partial=True
    )
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def lists_list(request, pk):
    """Listar as listas"""
    try:
        serializer = ListsManagementListSerializer(
            lists_id=pk
        )
        return JsonResponse(serializer.data)
    except Userlist.DoesNotExist:
        return Response(
            f"Não existe Lists com ID..{pk}",
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def list_create(request):
    username = request.data['username']
    try:
        title = request.data["item"]
        description = request.data['description']
    except Exception:
        return Response(
            "É necessário informar ITEM para a lista",
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            f"User..{username} não existe!",
            status=status.HTTP_400_BAD_REQUEST
        )
    request.data['user'] = user.id
    serializer = ListCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        id_list = serializer.data["id"]
        Item.objects.create(
            title=title,
            description=description,
            userlist_id=id_list,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def list_delete(request, pk):
    # if not self.user_has_permission():
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    list = Userlist.objects.filter(id=pk)
    list.delete()
    return Response(status.HTTP_200_OK)


@api_view(["GET"])
def item_list(request, pk):
    """Listar os itens da lista específica"""
    try:
        serializer = ItensManagementListSerializer(
            lists_id=pk
        )
        return JsonResponse(serializer.data)
    except Item.DoesNotExist:
        return Response(
            f"Não existe Item com ID..{pk}",
            status=status.HTTP_400_BAD_REQUEST
        )

# @api_view(["GET"])
# def users_list(request, pk):
#     """Listar os usuários"""
#     request_data = request.data
#     if request.method == "GET":
#         users = Usuary.objects.filter(id=pk)
#         serializer = UserListSerializer(
#             users,
#             data=request_data,
#             partial=True
#         )
#         if serializer.is_valid():
#             return Response(
#                 serializer.data, status=status.HTTP_200_OK
#             )
#         return Response(
#                 f"Nenhum informação com esse ID..: {pk}",
#                 status=status.HTTP_400_BAD_REQUEST
#         )
