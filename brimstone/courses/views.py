from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class CourseListView(ListView):
    template_name='list_course.html'
    queryset = Course.Objects.all()
    

