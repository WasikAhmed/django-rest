from rest_framework import serializers
from .models import TodoList, TodoTask


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = '__all__'
