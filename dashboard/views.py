from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddInfoForm
from .models import Transport

def dashboad(request):
    transportInfo = Transport.objects.all();
    return render(request, 'dashboad.html', {'transportInfo':transportInfo})

def addInfoPage(request):
    if request.method == "POST":
        form = AddInfoForm(request.POST)
        if form.is_valid():
            form = form.save()
            return render(request,'dashboad.html')

    else :
        form = AddInfoForm()
        return render(request, 'add-info-page.html', { 'form' : form})
