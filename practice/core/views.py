from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import BookNameFilterForm
from .models import Book
from .filters import BookFilter
from django.views.generic.list import ListView
# Create your views here.
def home(request):
    # name = request.GET.get('name')
    # books = Book.objects.all()
    # if name:
    #     books = books.filter(name__icontains = name)
    # print(name)

    # context = {
    #     'form':BookNameFilterForm,
    #     'books':books
    # }
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'form':book_filter.form,
        'books':book_filter.qs
    }
    return render(request,'index.html',context=context)

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context