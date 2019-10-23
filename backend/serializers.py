from rest_framework import serializers

# we need models to serialize from 
from .models import Event

from django import forms 


class EventSerializer(serializers.ModelSerializer):
     class Meta:
        model = Event
        fields = (
         'title', 'post','location', 'url' 
        )


