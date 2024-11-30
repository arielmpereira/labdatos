from django.shortcuts import render, get_object_or_404
from .models import Tutorial

# Create your views here.
def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'tutoriales/detail.html', {'tutorial': tutorial})


