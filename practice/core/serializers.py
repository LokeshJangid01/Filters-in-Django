from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author')

    class Meta:
        model = Book
        fields = (
            'name',
            'author_name',
            'price',
            'genre'

            )