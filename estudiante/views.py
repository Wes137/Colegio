from django.shortcuts import render
from .models import estudiante


def vista_estudiante(request):
    estudiantes = estudiante.objects.all()
    context = {
        'estudiante': estudiantes
    }
    return render(request, 'estudiante.html', context=context)