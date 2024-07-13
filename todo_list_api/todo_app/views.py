from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from .models import TodoList, TodoTask
from .serializers import TodoListSerializer, TodoTaskSerializer, UserSerializer
from django.contrib.auth.models import User


class TodoPagination(PageNumberPagination):
    page_size = 5


class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    pagination_class = TodoPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)


class TodoTaskView(generics.ListCreateAPIView):
    serializer_class = TodoTaskSerializer
    pagination_class = TodoPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoTask.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        todo_list = serializer.validated_data.get('todo_list')
        if todo_list and todo_list.user != self.request.user:
            raise serializers.ValidationError('You can only assign tasks to you own lists.')
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class TodoTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoTask.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=205)
        except TokenError as e:
            return Response({"detail": str(e)}, status=400)
