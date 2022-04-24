"""Courses and its related models are listed here. Registered 
for the admin panel. Every subject list_display shows its name and 
teacher(every subject has only one teacher in this school.)"""
from django.contrib import admin
from .models import Course, Lesson, Subject, Room, DayTime


admin.site.register(Course)
admin.site.register(Lesson)
# admin.site.register(Subject)
admin.site.register(Room)
admin.site.register(DayTime)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'course')
