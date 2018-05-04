from django.db import models

# Create your models here.


class Alarm(models.Model):
    name = models.CharField(max_length=20)
    minutes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        if self.status:
            return True
        return False