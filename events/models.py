from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50, help_text='Title of the event')
    time = models.DateTimeField('Time of the event', help_text='Time of the event')
    description = models.TextField('Description of the event', help_text='Description of the event', blank=True, null=True)

    def __str__(self):
        return self.title
    def is_complete(self):
        """ Checks if the event has passed"""
        return self.time < timezone.now()