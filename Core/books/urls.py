from django.urls import path
from .views import IndexView, BookDetailsView, BookListView, AddBookView, EditBookView

app_name = 'books'

urlpatterns = [
    #path('', IndexView.as_view(), name="books"),
    path('', BookListView.as_view(), name="book_list"),
    path('add/', AddBookView.as_view(), name="book_add"),
    path('<slug:slug>/', BookDetailsView.as_view(), name="book-detail"),
    path('<slug:slug>/edit/', EditBookView.as_view(), name="book_edit"),
]