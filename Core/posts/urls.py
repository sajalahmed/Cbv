from django.urls import path
from .views import PostView, PostRedirect, PostDetails

app_name = 'posts'

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('url/<int:pk>/', PostRedirect.as_view(), name="go-to"),
    path('details/<int:pk>/', PostDetails.as_view(), name='post_details'),
]