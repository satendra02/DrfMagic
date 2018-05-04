from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from notification.models import Alarm
from notification.serializers import AlarmSerializer


class AlarmViewset(viewsets.ModelViewSet):

    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer
