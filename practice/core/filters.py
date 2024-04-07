import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Book
        fields = {
                   'name':['icontains'],
                   'author__name':['icontains'], 
                   
                   'genre':['exact']
                }
