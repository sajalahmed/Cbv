from django.urls import path
from .views import UserView, userTest, userTest2

app_name = 'users'

urlpatterns = [
    path('users', UserView.as_view(), name="users"),
    path('test', userTest, name="user_test"),
    path('test/<item>/', userTest2, name="user_test2")
]