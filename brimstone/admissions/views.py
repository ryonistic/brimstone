from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AdmissionRequestForm


class RequestAdmissionView(CreateView):
    template_name = 'request_admission.html'
    form_class = AdmissionRequestForm
    success_url = reverse_lazy('home')
    success_message = 'Request Received. You will receive an email upon confirmation.'
