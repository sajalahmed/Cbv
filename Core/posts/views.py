from django.shortcuts import render
from .models import Category
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.views.generic.detail import DetailView

# Create your views here.

class PostView(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=1)
        context['data'] = "Extra data pass"
        return context

class PostRedirect(RedirectView):
    #url = 'https://facebook.com'
    pattern_name = 'posts:post_details'
    def get_redirect_url(self, *args, **kwargs):
        post = Category.objects.filter(pk=kwargs['pk'])
        post.update(count = F('count') + 1)
        return super().get_redirect_url(*args, **kwargs)


class PostDetails(TemplateView):
    template_name = "post_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return context

