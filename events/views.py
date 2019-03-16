from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return the created events by order of time"""
        return Event.objects.order_by('time')

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.email = request.user.email
            event.save()
            return redirect('events:detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})

class EventDeleteView(DeleteView):
    model = Event
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('events:index')

class EventUpdateView(UpdateView):
    model = Event
    fields = ['time','title','description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('events:index')