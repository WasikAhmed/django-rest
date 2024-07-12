from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoTask(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.description
