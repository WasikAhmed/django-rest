from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TodoListView, TodoListDetailView, TodoTaskView, TodoTaskDetailView, RegisterView, LogoutView

urlpatterns = [
    path('lists/', TodoListView.as_view(), name='todo-lists'),
    path('lists/<int:pk>/', TodoListDetailView.as_view(), name='todo-list-detail'),
    path('tasks/', TodoTaskView.as_view(), name='todo-tasks'),
    path('tasks/<int:pk>/', TodoTaskDetailView.as_view(), name='todo-task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
