from django.shortcuts import render
from pullups.forms import PullupForm
from pullups.models import Pullup



def home(request):
    if(request.GET.get('delete_btn')):
        Pullup.objects.all().delete()

    if request.method == 'POST':
        form = PullupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PullupForm()
    return render(request, 'pullups/home.html', {'form': form})

def view_history(request):
    if(request.GET.get('delete_btn')):
        Pullup.objects.all().delete()
    history = Pullup.objects.all()
    return render(request, 'pullups/view_history.html', {'history': history})

def graph(request):
    if(request.GET.get('delete_btn')):
        Pullup.objects.all().delete()
    history = Pullup.objects.all()
    return render(request, 'pullups/graph.html', {'history': history})

def to_do(request):
    return render(request, 'pullups/to_do.html')