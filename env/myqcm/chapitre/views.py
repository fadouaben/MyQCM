from django.shortcuts import render, get_object_or_404, redirect
from .models import Chapitre, Score
from .form import ChapitreForm, ScoreForm

# Chapitre views
def chapitre_list(request):
    chapitres = Chapitre.objects.all()
    return render(request, 'chapitre/interfaces/chapitre_list.html', {'chapitres': chapitres})

def chapitre_detail(request, pk):
    chapitre = get_object_or_404(Chapitre, pk=pk)
    return render(request, 'chapitre/interfaces/chapitre_detail.html', {'chapitre': chapitre})

def chapitre_create(request):
    if request.method == 'POST':
        form = ChapitreForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('chapitre_list')
    else:
        form = ChapitreForm()
    return render(request, 'chapitre/interfaces/chapitre_form.html', {'form': form})

def chapitre_update(request, pk):
    chapitre = get_object_or_404(Chapitre, pk=pk)
    if request.method == 'POST':
        form = ChapitreForm(request.POST, request.FILES, instance=chapitre)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('chapitre_list')
    else:
        form = ChapitreForm(instance=chapitre)
    return render(request, 'chapitre/interfaces/chapitre_update.html', {'form': form})

def chapitre_delete(request, pk):
    chapitre = get_object_or_404(Chapitre, pk=pk)
    if request.method == 'POST':
        chapitre.delete()
        return redirect('chapitre_list')  # Redirect to the list view
    return redirect('chapitre_list')  # Redirect to the list view if not POST

# Score views
def score_list(request):
    scores = Score.objects.all()
    return render(request, 'chapitre/interfaces/score_list.html', {'scores': scores})

def score_detail(request, pk):
    score = get_object_or_404(Score, pk=pk)
    return render(request, 'chapitre/interfaces/score_detail.html', {'score': score})

def score_create(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('score_list')
    else:
        form = ScoreForm()
    return render(request, 'chapitre/interfaces/score_form.html', {'form': form})

def score_update(request, pk):
    score = get_object_or_404(Score, pk=pk)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('score_list')
    else:
        form = ScoreForm(instance=score)
    return render(request, 'chapitre/interfaces/score_form.html', {'form': form, 'score': score})

def score_delete(request, pk):
    score = get_object_or_404(Score, pk=pk)
    if request.method == 'POST':
        score.delete()
        return redirect('score_list')
    return render(request, 'chapitre/interfaces/score_confirm_delete.html', {'score': score})
