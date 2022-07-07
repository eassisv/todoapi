from rest_framework import serializers

from todos.models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "todo", "done", "limit_date", "todo_list", "created_at"]
        extra_kwargs = {
            "todo_list": {
                "style": {"base_template": "input.html", "input_type": "number"}
            }
        }

    def validate_todo_list(self, todo_list):
        user = self.context["request"].user
        if todo_list not in user.todo_lists.all():
            raise serializers.ValidationError("user is not todo list owner")
        return todo_list


class SimpleTodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["id", "name"]


class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ["id", "name", "todos", "created_at"]
