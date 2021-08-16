from django.contrib import admin
from django.db import models
from books.models import Book

# Register your models here.

admin.site.register(Book)