from django.shortcuts import render
from .models import Category
from django.views.generic import TemplateView

# Create your views here.

class PostView(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['data'] = "Extra data pass"
        return context