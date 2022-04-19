from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CreatePostForm
from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'date_of_closing':'24th of June', 'posts':posts})

@login_required
def createpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreatePostForm(request.POST,  request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                messages.success(request, 'Post created successful.')
                return redirect('home')
            else:
                messages.success(request, 'There was an error with your entries.')
                return redirect('createpost')
        else:
            form = CreatePostForm()
        return render(request, 'createpost.html', {'form':form})
    else:
        return redirect('login')


def postdetail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'postdetail.html', {'post':post})
