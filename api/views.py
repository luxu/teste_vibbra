from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Book
from .serializer import MoedaListSerializer


@api_view(["GET"])
def books_list(request):
    """Listar os livros"""
    if request.method == "GET":
        books = Book.objects.all()
        serializer = MoedaListSerializer(books, many=True)
        return Response(serializer.data)
