from django.urls import path
from . import views


urlpatterns = [
        path('', views.RequestAdmissionView.as_view(), name="request_admission"),
        path('document_submission/', views.document_submission, name="document_submission"),
        path('admission_status/', views.admission_status, name="admission_status"),
        ] 
