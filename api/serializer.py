from django.contrib.auth.models import User
from rest_framework import serializers

from backend.base.models import Userlist, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "email",
            "password"
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
            "password"
        )


class UsersManagementSerializer(serializers.ModelSerializer):
    """A serializer for the Users model"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "email",
        )


class ListsManagementSerializer(serializers.ModelSerializer):
    """A serializer for the Lists model"""
    nome_do_usuario = serializers.ReadOnlyField(
        source="user.username", read_only=True
    )

    class Meta:
        model = Userlist
        fields = (
            "id",
            "title",
            "nome_do_usuario",
        )


class ListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlist
        fields = (
            "id",
            "title",
            "user",
        )


class ItemManagementSerializer(serializers.ModelSerializer):
    """A serializer for the Item model"""

    class Meta:
        model = Item
        fields = (
            "id",
            # "name",
            # "nome_do_usuario",
        )


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
        )


class ListsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlist
        fields = ("name", "user")


class ListsManagementListSerializer(serializers.ModelSerializer):
    """A serializer class for the Lists model"""

    def __init__(self, lists_id=None):
        self.lists_id = lists_id

    @property
    def data(self):
        if self.lists_id is not None:
            return self.lists_details(lists_id=self.lists_id)
        else:
            return self.list_lists(self.list_lists)

    @classmethod
    def lists_details(self, lists_id=None):
        lists = Userlist.objects.get(id=lists_id)
        serializer = ListsManagementSerializer(lists)
        return serializer.data

    def list_lists(self, token):
        serialized_enrollments = []
        for item in self.list_lists:
            lists = Userlist.objects.get(id=item.id)
            serialized_enrollments.append(
                self.lists_details(lists_id=lists.id)
            )
        return serialized_enrollments

    class Meta:
        model = Userlist
        fields = (
            "id",
            "name"
        )


class UsersManagementListSerializer(serializers.ModelSerializer):
    """A serializer class for the Lists model"""

    def __init__(self, user_id=None):
        self.user_id = user_id

    @property
    def data(self):
        if self.user_id is not None:
            return self.user_details(user_id=self.user_id)
        else:
            return self.user_lists(self.user_lists)

    @classmethod
    def user_details(self, user_id=None):
        lists = User.objects.get(id=user_id)
        serializer = UsersManagementSerializer(lists)
        return serializer.data

    def user_lists(self, token):
        serialized_enrollments = []
        for item in self.user_lists:
            lists = Userlist.objects.get(id=item.id)
            serialized_enrollments.append(
                self.user_details(lists_id=lists.id)
            )
        return serialized_enrollments

    class Meta:
        model = Userlist
        fields = ("id",)


class ItensManagementListSerializer(serializers.ModelSerializer):
    """A serializer class for the Lists model"""

    def __init__(self, lists_id=None):
        self.lists_id = lists_id

    @property
    def data(self):
        if self.lists_id is not None:
            return self.item_details(lists_id=self.lists_id)
        else:
            return self.itens_lists(self.lists_id)

    @classmethod
    def item_details(self, lists_id=None):
        itens = Item.objects.filter(lists__id=lists_id)
        serializer = ItemManagementSerializer(itens)
        return serializer.data

    def itens_lists(self, token):
        serialized_enrollments = []
        for item in self.lists_id:
            lists = Userlist.objects.get(id=item.id)
            serialized_enrollments.append(
                self.listsItem_details(lists_id=lists.id)
            )
        return serialized_enrollments

    class Meta:
        model = Userlist
        fields = ("id",)
