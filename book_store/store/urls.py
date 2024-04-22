from django.urls import path
from store import views

urlpatterns = [
    path('', views.books_list, name='book_list'),
]