from django.shortcuts import render
from .models import clase


def vista_clase(request):
    clases = clase.objects.all()
    context = {
        'clases': clases
    }
    return render(request, 'clase.html', context=context)