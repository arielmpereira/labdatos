from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.curso_detail, name='curso_detail'),
]
