from django.urls import path
from .views import IndexView, BookDetailsView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name="books"),
    path('<slug:slug>/', BookDetailsView.as_view(), name="book-detail"),
]