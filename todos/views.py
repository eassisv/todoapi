from rest_framework import generics, viewsets, permissions

from .models import Todo, TodoList
from .serializers import SimpleTodoListSerializer, TodoListSerializer, TodoSerializer
from .permissions import IsOwner


class TodoListViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = TodoListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.todo_lists

    def get_serializer_class(self):
        if self.action == "list":
            return SimpleTodoListSerializer
        return TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_todo_lists = self.request.user.todo_lists.all()
        return Todo.objects.filter(todo_list__in=user_todo_lists)
