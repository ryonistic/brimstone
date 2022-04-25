"""All the urls related to Post creation and Detail view are listed here."""
from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('about/', views.AboutView.as_view(), name="about"),
        path('research/', views.ResearchView.as_view(), name="research"),
        path('createpost/', views.createpost, name="createpost"),
        path('postdetail/<slug>/', views.postdetail, name="postdetail"),

        ]
