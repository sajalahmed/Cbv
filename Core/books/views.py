from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.utils import timezone

from .models import Book
from .forms import AddForm

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django_redis import get_redis_connection
from django.utils.decorators import method_decorator


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

class BookListViewExtra(ListView):
    model = Book
    template_name = "book/list.html"
    context_object_name = "books"     #default object_list
    paginate_by = 4
    #queryset = Book.objects.all()[:2]
    #or method
    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(title__icontains=self.kwargs.get('title')) #__icontains for case sensitive search
