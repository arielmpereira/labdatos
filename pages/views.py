from django.shortcuts import render

# Create your views here.

def acerca_de(request):
    return render(request, 'pages/acerca_de.html')

def contacto(request):
    return render(request, 'pages/contacto.html')