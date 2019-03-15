from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Event
from .forms import EventForm

def index(request):
    event_list = Event.objects.order_by('time')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=form.id)
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})