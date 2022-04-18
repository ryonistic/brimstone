from django.db import models
from django.conf import settings


class Course(models.Model):
    """ This is a model for adding courses in the database"""
    STREAM_CHOICES = (
            ('1','Science'),
            ('2','Arts'),
            ('3','Sports'),
            ('4','Others'),
            )
    name = models.CharField(max_length=120)
    duration = models.PositiveIntegerField(default=4)
    description = models.TextField()
    hod = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    stream = models.CharField(choices = STREAM_CHOICES, max_length=55)

    def __str__(self):
        return self.name
