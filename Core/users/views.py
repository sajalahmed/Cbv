from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.

class UserView(TemplateView):
    template_name = "users.html"
