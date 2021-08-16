from typing import List
from django.urls import path
from todos.views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='todo-details'),
    path('', ListTodo.as_view(), name='todo-list'),
]
