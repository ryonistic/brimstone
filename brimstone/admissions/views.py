"""This view handles admission requests as well as document DocumentSubmissionForm
and verification. Once documents are verified, the admission application status is 
changed to completed and the document and application are used to create a Student
instance in the database."""
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from admissions.models import Admission, Document
from students.models import Student
from .forms import AdmissionRequestForm, DocumentSubmissionForm

class RequestAdmissionView(SuccessMessageMixin, CreateView):
    """After the user enters their info and submits the request, they receieve
    an email with their application id(which is a UUID) as a token. They may use 
    this token to submit their documents to the website for verification."""
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

def document_submission(request):
    """When submitting documents, the user needs to enter the application ID 
    They upload all the necessary files and then post the form. Website receives 
    the form and thus, creates a Document object in the database. This instance is 
    to be verified by an admission officer."""
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
    """User may check their admission application status by entering 
    the admission application ID they received in the email. This id will
    show their current admission status and whether they have submitted their documents
    and whether their verification is pending."""
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
    """This page is visible only to admins and they may approve documents from this page 
    This page only shows list of the documents. It may be configured to show all the files too. 
    But that is left up to the admins to decide."""
    if request.user.is_superuser:
        documents = Document.objects.filter(verified=False)
        return render(request, 'document_verification.html', {'documents':documents})
    else:
        messages.success(request, 'Not allowed.')
        return redirect('home')

def approve_document(request, document_id):
    """Admins may approve certain documents and change their 
    status to verified. Once that happens, a Student instance is 
    created in the database that has all the same details as the original
    application and document submission. It also changes the adm(admission application)
    status to COMPLETED which was originally set to PENDING. Also, it sends an email to 
    the student upon successful verification."""
    if request.user.is_superuser:
        document = get_object_or_404(Document, id=document_id)
        document.verified = True
        document.save()
        adm = document.application 
        adm.status = '1'
        adm.save()
        send_mail(
        'Documents Approved',
        f'Congratulations {document.application.student_name}! Your documents have been approved.\
                You may download your timetable from the below link.',
        'from@example.com',
        [str(document.application.email)],
        fail_silently=False,
        )
        new_student = Student.objects.create(
                name=document.application.student_name,
                email=document.application.email,
                phone = document.application.phone,
                course=document.application.course,
                date_of_birth=document.application.date_of_birth,
                father_name= document.application.father_name,
                mother_name = document.application.mother_name,
                gender = document.application.gender,
                address = document.application.address,
                state = document.application.state,
                student_photo = document.student_photo,
                highschool_diploma = document.highschool_diploma,
                address_proof = document.address_proof,
                undertaking = document.undertaking,
                )  
        new_student.save()
        messages.success(request, 'Document verification complete')
        return redirect('document_verification')
    else:
        messages.success(request, 'Not allowed.')
        return redirect('home')
