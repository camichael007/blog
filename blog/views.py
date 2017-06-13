from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.

def index(request):
    tpl = loader.get_template('index.html')
    context = Context({'name':'michael', 'age':25})
    return HttpResponse(tpl.render(context))
