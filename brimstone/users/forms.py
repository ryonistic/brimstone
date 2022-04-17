from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'p-2 m-2', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'p-2 m-2', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'p-2 m-2', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''
            self.fields[fieldname].widget.attrs['class']='p-2 m-2'

        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password1'].widget.attrs['placeholder']='Enter Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
