from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from admissions.models import Admission, Document
from .forms import AdmissionRequestForm, DocumentSubmissionForm

class RequestAdmissionView(SuccessMessageMixin, CreateView):
    template_name = 'request_admission.html'
    form_class = AdmissionRequestForm
    success_message = 'Request Received. You will receive an email upon confirmation.'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        student = form.cleaned_data['student_name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        applicationid = Admission.objects.get(email=email, student_name=student, phone=phone)
        send_mail(
            'Documents Approved',
            f'Greetings {student}! Your application has been Received. You may submit your documents on our website at Nav>Admission>Documentation.Your token is the same as your ApplicationID i.e. {applicationid}',
            'from@example.com',
            [str(email)],
            fail_silently=False,
            )
        messages.success(self.request, 'Request Received. You will receive an email upon confirmation.')
        return HttpResponseRedirect(self.get_success_url())


# def request_admission(request):
#     if request.method == "POST":
#         form = AdmissionRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             student = form.cleaned_data['student_name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             applicationid = Admission.objects.get(email=email, student_name=student, phone=phone)
#             send_mail(
#                 'Documents Approved',
#                 f'Greetings {student}! Your application has been Received. You may submit your documents on our website at Nav>Admission>Documentation.Your token is the same as your ApplicationID i.e. {applicationid}',
#                 'from@example.com',
#                 [str(email)],
#                 fail_silently=False,
#                 )
#             messages.success(request, 'Request Received. You will receive an email upon confirmation.')
#             return redirect('home')
#         else:
#             messages.success(request, 'Error in submission. Try again.')
#             return redirect('request_admission')
#     else:
#         form = AdmissionRequestForm
#         return render(request, 'request_admission.html', {'form':form})

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
        return render(request, 'admission_status.html',\
                {'document':document, 'application':application, 'get_req':get_req})
    else:
        get_req = True
        return render(request, 'admission_status.html', {'get_req':get_req})

def document_verification(request):
    if request.user.is_superuser:
        documents = Document.objects.filter(verified=False)
        return render(request, 'document_verification.html', {'documents':documents})
    else:
        messages.success(request, 'Not allowed.')
        return redirect('home')

def approve_document(request, document_id):
    if request.user.is_superuser:
        document = get_object_or_404(Document, id=document_id)
        document.verified = True
        document.save()
        send_mail(
        'Documents Approved',
        f'Congratulations {document.application.student_name}! Your documents have been approved.\
                You may download your timetable from the below link.',
        'from@example.com',
        [str(document.application.email)],
        fail_silently=False,
        )
        messages.success(request, 'Document verification complete')
        return redirect('document_verification')
    else:
        messages.success(request, 'Not allowed.')
        return redirect('home')
