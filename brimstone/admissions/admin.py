from django.contrib import admin
from .models import Admission, Document

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'admission_id', 'email')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('get_student_name' , 'application', 'verified')

    @admin.display(description='Student')
    def get_student_name(self, obj):
        return obj.application.student_name
