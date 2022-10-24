from django.forms import modelform_factory
from django.shortcuts import redirect, render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona
from personas.forms import PersonaForm

def detallePersona(request, id):
    persona = get_object_or_404 (Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

# PersonaForm = modelform_factory(Persona, exclude=[])
    
def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
        
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
        
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')