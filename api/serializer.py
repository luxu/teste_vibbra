from rest_framework import serializers

from library.models import Book


class MoedaListSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.name", read_only=True)

    class Meta:
        model = Book
        fields = ("title", "author", )
