from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gymlog.models import Day, Exercise, Instance
from gymlog.forms import InstanceForm

import os

def dev(request):
    '''
    Things useful for development; only displayed in DEBUG mode
    '''
    from youthinasia import settings

    items = []
    db = settings.DATABASES

    items.append(db)
    items.append(os.getcwd().split())

    return render(request, 'gymlog/dev.html', {'items': items})

def home(request):
    '''
    List all the days in the current Routine.
    '''
    days = Day.objects.all()

    return render(request, 'gymlog/home.html', {'days': days})

def day(request, slug):
    '''
    Show all of the exercises in a particular day
    '''
    day = get_object_or_404(Day, slug=slug)
    exercises = day.exercise_set.all()
    return render(request, 'gymlog/day_details.html', {'exercises': exercises})

def exercise(request, slug):
    '''
    Splash page for an exercise, shows the most recent entry and a form for the next entry.
    '''
    exercise = get_object_or_404(Exercise, slug=slug)

    # A little history to show
    history = Instance.objects.filter(exercise_id = exercise.id)

    # Form
    if request.method == 'POST':
        form = InstanceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.exercise_id = exercise.id
            instance.save()
            url = reverse('gymlog:form_success', args=())
            return HttpResponseRedirect(url)
    else:
        form = InstanceForm()
    return render(request, 'gymlog/exercise_form.html',
                  {'form': form,
                   'exercise': exercise,
                   'history': history})

def form_success(request):
    return render(request, 'gymlog/form_success.html')