"""Two simple urls that list and detail course details."""
from django.urls import path
from . import views

urlpatterns = [
        path('',views.CourseListView.as_view(), name="courses"),
        path('<int:course_id>/',views.CourseDetailView.as_view(), name="course_detail")

        ]
