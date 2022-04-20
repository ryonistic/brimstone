from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from courses.models import Course, Lesson, Subject, Room, DayTime


@login_required
def dashboard(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'dashboard.html', {})
    else:
        messages.success(request, 'You are not a staff member!')
        return redirect('home')
