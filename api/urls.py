from django.urls import path
from .views import RegisterView, LoginView, QueryView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("kb/query/", QueryView.as_view(), name="kb-query"),
]