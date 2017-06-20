from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
import datetime
# Create your views here.

def index(request):
    tpl = loader.get_template('index.html')
    context = Context({'name':'michael', 'age':25})
    return HttpResponse(tpl.render(context))

def mail_thank(request):
    tpl = loader.get_template("thanks_mail.html")
    context = Context({'person_name':'michael',
                       'company':'juanpi',
                       'ship_date':datetime.datetime.now(),
                       'item_list':['apple', 'pear', 'watermelon', 'strawberry'],
                       'ordered_warranty':False,
                       })
    return HttpResponse(tpl.render(context))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now%s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    assert False
    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hours, it will be %s.</body></html>' %(offset, time)
    return HttpResponse(html)