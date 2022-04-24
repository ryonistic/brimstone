"""All the urls related to Post creation and Detail view are listed here."""
from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('createpost/', views.createpost, name="createpost"),
        path('postdetail/<slug>/', views.postdetail, name="postdetail"),

        ]
