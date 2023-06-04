from django.shortcuts import redirect, render
from visiteCandidats.models import Candidats
from visiteCandidats.forms import CandidatFrom
#insertions des données
def cdt(request):
    if request.method=="POST":
        form=CandidatFrom(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=CandidatFrom()
    return render(request, 'index.html', {'form':form})
#Affichage des données
def show(request):
    allcandidats = Candidats.objects.all()
    return render(request, 'show.html', {'allcandidats':allcandidats})
#Détails
def edit(request,id):
    editcandidats = Candidats.objects.get(id=id)
    return render(request, 'edit.html', {'editcandidats':editcandidats})
#Modification des données
def update(request,id):
    editcandidats = Candidats.objects.get(id=id)
    form=CandidatFrom(request.POST, instance=editcandidats)
    if form.is_valid():
            form.save()
            return redirect("/show")
    return render(request, 'edit.html', {'editcandidats':editcandidats})
#Supperssion des données
def delete(request,id):
    delcandidats = Candidats.objects.get(id=id)
    delcandidats.delete()
    return redirect("/show")