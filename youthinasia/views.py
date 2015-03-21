__author__ = 'clint'

import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from forms import Basic_Form

def hello(request):
    return render(request, 'hello.html')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>in %s hours, it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def gym(request):
    return HttpResponse("<html><body> gym test... </body></html>")

def form_page(request):
    if request.method == 'POST':
        form = Basic_Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect(reverse('/thanks/'))
    else:
        form = Basic_Form(initial={'subject': 'enter shit here'})
    return render(request, 'form.html', {'form': form})

def thanks(request, **kwargs):
    msg = kwargs
    return render(request, 'thanks.html', {'msg': msg})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))