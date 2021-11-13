from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.utils import timezone

from .models import Book

class IndexView(TemplateView):
    template_name = "book/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


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
