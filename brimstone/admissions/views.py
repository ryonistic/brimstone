from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from admissions.models import Admission, Document

from .forms import AdmissionRequestForm, DocumentSubmissionForm


class RequestAdmissionView(SuccessMessageMixin, CreateView):
    template_name = 'request_admission.html'
    form_class = AdmissionRequestForm
    success_message = 'Request Received. You will receive an email upon confirmation.'
    success_url = reverse_lazy('home')
#
#
# class DocumentSubmissionView(CreateView):
#     template_name = 'document_submission.html'
#     form_class = DocumentSubmissionForm
#     success_url = reverse_lazy('home')
#     success_message = 'Documents Received. Verification may take upto 48 hours.'

def document_submission(request):
    if request.method=='POST':
        form = DocumentSubmissionForm(request.POST, request.FILES)
        applicationID = request.POST['application_id']
        if form.is_valid():
            document = form.save(commit=False)
            try:
                admission_form_id = Admission.objects.get(admission_id = applicationID)
            except ObjectDoesNotExist:
                admission_form_id = None
            if admission_form_id is not None:
                document.application = admission_form_id
            else:
                messages.success(request, 'That Application ID does not exist.')
                return redirect('document_submission')
            try:
                document.save()
                messages.success(request, 'Documents Received. Verification may take upto 48 hours.')
                return redirect('home')
            except Exception:
                messages.success(request, "It seems you have already submitted your documents.")
                return redirect('home')
        else:
            messages.success(request, 'Please enter the correct details.')
            return redirect('document_submission')
    else:
        form = DocumentSubmissionForm
        return render(request, 'document_submission.html', {'form':form})

def admission_status(request):
    if request.method == 'POST':
        get_req = False
        applicationID = request.POST['application_id']
        try:
            application = Admission.objects.get(admission_id=applicationID)
        except ObjectDoesNotExist:
           application =  None
        try:
            document = Document.objects.get(application=application)
        except ObjectDoesNotExist:
           document =  None
        return render(request, 'admission_status.html', {'document':document, 'application':application, 'get_req':get_req})
    else:
        get_req = True
        return render(request, 'admission_status.html', {'get_req':get_req})
