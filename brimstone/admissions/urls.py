from django.urls import path
from . import views


urlpatterns = [
        path('', views.request_admission, name="request_admission"),
        path('document_submission/', views.document_submission, name="document_submission"),
        path('admission_status/', views.admission_status, name="admission_status"),
        path('document_verification/', views.document_verification, name="document_verification"),
        path('approve_document/<int:document_id>/', views.approve_document, name="approve_document"),
        ] 
