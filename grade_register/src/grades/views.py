from django.shortcuts import render
from .models import Grade

def grade_list(request):
    grades = Grade.objects.all()  # Obtener todas las calificaciones
    return render(request, 'grades/grade_list.html', {'grades': grades})
