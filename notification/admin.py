from django.contrib import admin

# Register your models here.
from notification.models import Alarm

admin.site.register(Alarm)