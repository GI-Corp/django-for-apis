from django.db import models
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from books.models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'