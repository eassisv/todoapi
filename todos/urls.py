from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("todo-lists", views.TodoListViewSet, basename="todo-lists")
router.register("todos", views.TodoViewSet, basename="todos")

app_name = "todos"
urlpatterns = [path("", include(router.urls))]
