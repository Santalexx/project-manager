from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

# @login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.gerente = request.user  # Asumiendo que tienes autenticación de usuario
            proyecto.save()
            return redirect('proyectos:lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'form': form})
