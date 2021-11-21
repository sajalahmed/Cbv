from django.urls import path
from .views import UserView, userTest

app_name = 'users'

urlpatterns = [
    path('users', UserView.as_view(), name="users"),
    path('test', userTest, name="user_test")
]