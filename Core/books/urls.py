from django.urls import path
from .views import IndexView, BookDetailsView, BookListView

app_name = 'books'

urlpatterns = [
    #path('', IndexView.as_view(), name="books"),
    path('', BookListView.as_view(), name="book_list"),
    path('<slug:slug>/', BookDetailsView.as_view(), name="book-detail"),
]