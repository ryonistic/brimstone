from django.contrib import admin
from .models import Admission, Document

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'admission_id', 'email')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'verified')
