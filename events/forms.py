from django.forms import ModelForm, DateTimeInput, DateTimeField
from .models import Event
from django.conf import settings

class EventForm(ModelForm):
    class Meta:
        model = Event
        time = DateTimeField(required=True, input_formats=settings.DATETIME_INPUT_FORMATS)
        fields = ('title', 'time', 'description',)