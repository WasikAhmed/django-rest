from django.contrib import admin
from .models import TodoList, TodoTask

# Register your models here.
admin.site.register(TodoList)
admin.site.register(TodoTask)
