from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('curso/', views.tutoriales, name='tutoriales'),
    path('desafios/', views.desafios, name='desafios'),
    path('datasets/', views.datasets, name='datasets'),
    path('comunidad/', views.comunidad, name='comunidad'),
]
