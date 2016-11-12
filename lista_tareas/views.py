from django.shortcuts import render
from django.utils import timezone
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lista_tareas/lista_tareas.html', {'tareas': tareas})
