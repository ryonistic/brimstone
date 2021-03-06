"""Students can be listed and viewed in the admin panel. """
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'email')
