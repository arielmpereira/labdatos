from django.shortcuts import render
from curso.models import Tutorial
# from desafios.models import Desafio
# from datasets.models import Dataset
# from community.models import Post

# Create your views here.
def home(request):
    # Obtener los datos destacados de cada sección
    tutoriales_destacados = Tutorial.objects.all()[:3]
    desafios_destacados = Desafio.objects.all()[:3]
    datasets_destacados = Dataset.objects.all()[:3]
    posts_recientes = Post.objects.order_by('-created_at')[:3]

    return render(request, 'core/home.html', {
        'tutoriales_destacados': tutoriales_destacados,
        'desafios_destacados': desafios_destacados,
        'datasets_destacados': datasets_destacados,
        'posts_recientes': posts_recientes,
    })

def tutoriales(request):
    # Delegar a la app tutoriales para obtener el contenido
    return render(request, 'core/tutoriales.html')

def desafios(request):
    # Delegar a la app desafios para obtener el contenido
    return render(request, 'core/desafios.html')

def datasets(request):
    # Delegar a la app datasets para obtener el contenido
    return render(request, 'core/datasets.html')

def comunidad(request):
    # Delegar a la app community para obtener el contenido
    return render(request, 'core/comunidad.html')