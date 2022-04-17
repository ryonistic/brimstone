from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'date_of_closing':'24th of June'})
