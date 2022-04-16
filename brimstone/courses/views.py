from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course


class CourseListView(ListView):
    template_name='list_courses.html'
    queryset = Course.objects.all()
    context_object_name = "courses"

class CourseDetailView(DetailView):
    template_name = 'course_detail.html'
    queryset = Course.objects.all()
    context_object_name = "course"
    pk_url_kwarg = "course_id"