from django.shortcuts import render
from travels.models import Travel



def index(request):
    travel = Travel.objects.all()
    return render(request, 'main/index.html', {'travel': travel})

def travels(request):
    return render(request, 'main/travels.html')