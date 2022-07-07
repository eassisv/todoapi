from django.urls import path

from .views import SignUpView, SingInView

app_name = "users"
urlpatterns = [
    path("signup/", SignUpView.as_view()),
    path("signin/", SingInView.as_view()),
]
