from django.shortcuts import render, get_object_or_404, redirect
from .models import Cours
from .forms import CoursForm

def cours_list(request):
    courss = Cours.objects.all()
    for cours in courss:
        print(cours.id)  # Debug print
    return render(request, 'list_cours.html', {'courss': courss})



def cours_detail(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    return render(request, 'detailcours.html', {'cours': cours})

def cours_create(request):
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm()
    return render(request, 'ajout_cours.html', {'form': form})

def cours_update(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'modifier_cours.html', {'form': form})

def cours_delete(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours_list')
    return redirect('cours_list')
