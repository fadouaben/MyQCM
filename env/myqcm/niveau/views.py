from django.shortcuts import render
from niveau.models import  Niveau
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import DeleteView,UpdateView,CreateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .form import NiveauForm
def afficher_niveau(request):
    niveaux = Niveau.objects.all()
    return render(request, 'niveau/liste_niveau.html', {'niveaux': niveaux})

    
class NiveauCreateView(CreateView):
    form_class=NiveauForm
    context='Niveau'
    model=Niveau
    template_name='niveau/NiveauCreate.html'
# Create your views here.
    def form_valid(self ,form, *args , **kwargs):
        form.save()
        return redirect('listeNiveaux')
    
def edit_niveau(request, niveau_id):
    niveau = get_object_or_404(Niveau, pk=niveau_id)

    if request.method == 'POST':
        form = NiveauForm(request.POST, instance=niveau)
        if form.is_valid():
            form.save()
            return redirect('listeNiveaux')  # Redirige après la modification vers la liste des matières
    else:
        form = NiveauForm(instance=niveau)

    return render(request, 'niveau/edit_niveau.html', {'form': form, 'ma': niveau})

def delete_niveau(request, niveau_id):
    niveau = get_object_or_404(Niveau, pk=niveau_id)

    if request.method == 'POST':
        niveau.delete()
        return redirect('listeNiveaux')  # Redirige après la suppression vers la liste des matières

    return render(request, 'niveau/delete_niveau.html', {'niveau': niveau})
# Create your views here.
