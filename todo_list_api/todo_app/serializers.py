from rest_framework import serializers
from .models import TodoList, TodoTask
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TodoTaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TodoTask
        fields = '__all__'

    def validate_todo_list(self, value):
        request = self.context['request']
        if value.user != request.user:
            raise serializers.ValidationError('You can only assign tasks to your own lists.')
        return value


class TodoListSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TodoList
        fields = '__all__'
