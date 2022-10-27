from django.http import HttpResponse

from django.shortcuts import render
from osoby.forms import UserLoginForm

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def info(request):
    return HttpResponse("<p>Cześć! Tworzymy aplikacje!</p>")

def loguj_osobe(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)