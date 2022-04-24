"""This app doesnt contain any models or the like YET.
In the future, if needed, we may add more details in the dashboard."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from courses.models import Lesson 


@login_required
def dashboard(request):
    if request.user.is_staff or request.user.is_superuser:
        lessons=Lesson.objects.filter(subject__teacher=request.user)

        return render(request, 'dashboard.html', {'lessons':lessons})
    else:
        messages.success(request, 'You are not a staff member!')
        return redirect('home')
