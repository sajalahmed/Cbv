from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.list import ListView

# Create your views here.

class UserView(TemplateView):
    template_name = "users.html"


class RommView(ListView):
    def get_context_data():
        

"""
* => single asterisk means unpack a list
** => double asterisk means uppack a dictornary 
"""


def add_number(a, b, c):
    print(a, b, c)

def __args(*args): #args work like touple and **kwargs work like dict
    print(args)

def __kwargs(**kwargs):
    print(kwargs)

def userTest(request):
    b =[3, 3, 3]
    add_number(*b)
    __args(1, 3, 5)
    val = {'a': 1, 'b': 2}
    __kwargs(a = 1, b = 2)
    #or
    __kwargs(**val)

    return render(request, 'test.html')

def userTest2(request, **kwargs):

    print(kwargs['item'])
    return render(request, 'test.html')    
