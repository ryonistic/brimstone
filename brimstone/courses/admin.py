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
