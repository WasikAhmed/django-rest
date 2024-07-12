from django.urls import path
from .views import TodoListView, TodoListDetailView, TodoTaskView, TodoTaskDetailView

urlpatterns = [
    path('lists/', TodoListView.as_view(), name='todo-lists'),
    path('lists/<int:pk>/', TodoListDetailView.as_view(), name='todo-list-detail'),
    path('tasks/', TodoTaskView.as_view(), name='todo-tasks'),
    path('tasks/<int:pk>/', TodoTaskDetailView.as_view(), name='todo-task-detail'),
]