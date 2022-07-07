from django.db import models
from django.conf import settings


class TodoList(models.Model):
    name = models.CharField(max_length=127)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todo_lists"
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_at"]


class Todo(models.Model):
    todo = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    limit_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name="todos"
    )

    class Meta:
        ordering = ["-updated_at"]
