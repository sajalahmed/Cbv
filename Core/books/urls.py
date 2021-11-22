from django.urls import path
from .views import IndexView, BookDetailsView, BookListView, AddBookView, EditBookView, BookListViewExtra, DataTable, TableView

app_name = 'books'

urlpatterns = [
    #path('', IndexView.as_view(), name="books"),
    path('', BookListView.as_view(), name="book_list"),
    path('table/view', TableView.as_view(), name="book_table"),
    path('table/list', DataTable.as_view(), name="book_table_list"),
    path('add/', AddBookView.as_view(), name="book_add"),
    path('<slug:slug>/', BookDetailsView.as_view(), name="book-detail"),
    path('<slug:slug>/edit/', EditBookView.as_view(), name="book_edit"),
]