from django.shortcuts import render
from matiere.models import  Matiere
from django.views.generic import DeleteView,UpdateView,CreateView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .form import MatiereForm
from .serializers import MatiereSerializer
def afficher_matiere(request):
    matieres = Matiere.objects.all()
    serializer = MatiereSerializer(matieres, many=True)
   

    
class MatierCreateView(CreateView):
    form_class=MatiereForm
    context='Matiere'
    model=Matiere
    template_name='matiere/MatiereCreate.html'
# Create your views here.
    def form_valid(self ,form, *args , **kwargs):
        form.save()
        return redirect('listeMatieres')
    
def edit_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, pk=matiere_id)

    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('listeMatieres')  # Redirige après la modification vers la liste des matières
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'matiere/edit_matiere.html', {'form': form, 'matiere': matiere})

def delete_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, pk=matiere_id)

    if request.method == 'POST':
        matiere.delete()
        return redirect('listeMatieres')  # Redirige après la suppression vers la liste des matières

    return render(request, 'matiere/delete_matiere.html', {'matiere': matiere})