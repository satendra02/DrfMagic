
from rest_framework import serializers

from notification.models import Alarm


class AlarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alarm
        fields = ('name', 'status', 'minutes',)