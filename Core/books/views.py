from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.utils import timezone

from .models import Book
from .forms import AddForm

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django_redis import get_redis_connection
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(TemplateView):
    template_name = "book/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

#FormView
"""
class AddBookView(FormView):
    template_name = "book/book_add.html"
    form_class = AddForm
    success_url = '/books/'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""
#Createview , we don't need to form validate in create view.
class AddBookView(CreateView):
    model = Book
    template_name = "book/book_add.html"
    form_class = AddForm
    success_url = '/books/'


    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['title'] = 'enter Title'
        return initial



class EditBookView(PermissionRequiredMixin, UpdateView):
    permission_required = 'books.change_books' # ('books.change_books', 'books.add_books')
    model = Book
    template_name = "book/book_edit.html"
    form_class = AddForm
    success_url = '/books/'

class BookDetailsView(DetailView):
    model = Book
    template_name = "book/book-details.html"
    context_object_name = "book"
    #if we not define context object name we can access ta through object.title or ect

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books = Book.objects.filter(slug=self.kwargs.get('slug'))
        context['time'] = timezone.now()
        return context

#@method_decorator(cache_page(60 * 5), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = "book/list.html"
    context_object_name = "books"
    paginate_by = 5

    """
    def get_queryset(self): #method to change the list of records returned
        return Book.objects.all()
    """
    def get_context_data(self, **kwargs):  #in order to pass additional context variables
        context = super().get_context_data(**kwargs)
        #context['books'] = Book.objects.all()[:2]
        return context

    def get_queryset(self, *args, **kwargs):
        title = self.kwargs.get('title')
        print(args)
        print(title)
        if title:
            return Book.objects.filter(title__icontains=self.kwargs.get('title')) #__icontains for case sensitive search
        context = super().get_queryset(*args, **kwargs)
        return context

class BookListViewExtra(ListView):
    model = Book
    template_name = "book/list.html"
    context_object_name = "books"     #default object_list
    paginate_by = 4
    #queryset = Book.objects.all()[:2]
    #or method

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs.get('title'))
        return Book.objects.filter(title__icontains=self.kwargs.get('title')) #__icontains for case sensitive search


class TableView(TemplateView):
    template_name = "book/datatable.html"

class DataTable(ListView):
    model = Book
    template_name = "book/ajax.html"
    context_object_name = "books"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        limit = self.request.GET.get('limit')
        _sl = 1
        _lm = 10
        if page:
            _sl = int(page)
        if limit:
            _lm = int(limit)
        context['sl_count'] = (_sl * _lm - (_lm - 1)) - 1
        
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('limit', self.paginate_by)    
