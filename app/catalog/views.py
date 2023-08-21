from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import  viewsets

from app.catalog.models.author import Author
from app.catalog.serializers.author import AuthorSerializer

class AuthorModelViewSet(viewsets.ModelViewSet):
    """
    作者的表

    ---
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer