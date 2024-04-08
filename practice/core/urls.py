from django.urls import path
from .views import home, BookListView

urlpatterns = [
    
    path('',BookListView.as_view(), name='index'),
]
