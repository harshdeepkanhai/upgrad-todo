from django.forms import ModelForm, DateTimeInput
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'time', 'description',)
        widgets  = {
          'time': DateTimeInput(attrs={'type': 'datetime-local'}, format='%m/%d/%y %H:%M:%S'),
        }