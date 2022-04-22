from django.urls import path
from . import views


urlpatterns = [
        path('', views.RequestAdmissionView.as_view(), name="request_admission"),
        ] 
