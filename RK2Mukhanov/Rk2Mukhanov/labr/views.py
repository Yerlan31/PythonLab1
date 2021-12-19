from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from Rk2Mukhanov.labr.models import myFile, myDirectory


def hello(request):
    return render(request, 'labr/index.html', {'current_date': date.today()})
# Create your views here.


def output(request):
    file = myFile.objects.all()
    directory = models.directoties
    content = {
        'folder': file,
        'directory': directory
    }
    return render(request, 'labr/html', )
