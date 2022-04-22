
from django import forms
from .models import Admission

class AdmissionRequestForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('student_name', 'date_of_birth', 'father_name', 'mother_name', \
                'qualification_level', 'email', 'phone', 'gender', 'address', 'state', 'course')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['student_name', 'date_of_birth', 'father_name', 'mother_name', \
                'qualification_level', 'email', 'phone', 'gender', 'address', 'state', 'course']:
            self.fields[fieldname].widget.attrs['class']='p-2 m-2 border border-2 rounded min-w-full'
            labelmaker = self.fields[fieldname].label
            self.fields[fieldname].widget.attrs['placeholder']=labelmaker
            self.fields[fieldname].label=''


