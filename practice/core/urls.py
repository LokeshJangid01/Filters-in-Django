from django.urls import path
from .views import home, BookListView,BookListApiView

urlpatterns = [
    
    path('',BookListView.as_view(), name='index'),
    path('api/',BookListApiView.as_view(), name='index'),
]
