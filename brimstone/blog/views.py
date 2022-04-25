"""You may create posts or view them on a detailed page.
Home page shows a list of the posts."""
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import CreatePostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'date_of_closing':'24th of June', 'posts':posts})

class AboutView(TemplateView):
    template_name='about.html'

class ResearchView(TemplateView):
    template_name='research.html'

@login_required
def createpost(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = CreatePostForm(request.POST,  request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                messages.success(request, 'Post created successfully.')
                return redirect('home')
            else:
                messages.success(request, 'There was an error with your entries.')
                return redirect('createpost')
        else:
            form = CreatePostForm()
        return render(request, 'createpost.html', {'form':form})
    else:
        return redirect('home')


def postdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'postdetail.html', {'post':post})
