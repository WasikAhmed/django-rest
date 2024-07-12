from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import TodoList, TodoTask
from .serializers import TodoListSerializer, TodoTaskSerializer


class TodoPagination(PageNumberPagination):
    page_size = 5


class TodoListView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    pagination_class = TodoPagination


class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoTaskView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
    pagination_class = TodoPagination


class TodoTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
