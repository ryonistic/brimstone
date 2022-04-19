from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
                'title' : forms.TextInput(attrs={'class':'p-2 border border-2 border-blue-600 rounded m-2'}),
                'content' : forms.TextInput(attrs={'class':'p-2 border border-2 border-blue-600 rounded m-2'}),
                }
