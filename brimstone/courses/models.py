"""This area is reserved for defining object instances for the database tables"""
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
        return str(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return str(self.number)

class DayTime(models.Model):
    DAY_CHOICES = (
            ('1','Monday'),
            ('2','Tuesday'),
            ('3','Wednesday'),
            ('4','Thursday'),
            ('5','Friday'),
            ('6','Saturday'),
            ('7','Sunday'),
            )

    day = models.CharField(choices = DAY_CHOICES, max_length=20)
    time = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.time) + "'o clock on " + str(self.DAY_CHOICES[int(self.day)-1][1])

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    time = models.ForeignKey(DayTime, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
