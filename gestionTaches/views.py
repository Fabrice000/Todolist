from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import tachesForm
from .models import Taches
from datetime import datetime

# Create your views here.

def home(request):
    taches_termined = []
    taches_no_termined = []
    taches = Taches.objects.all()[::-1]
    for tache in taches:
        if tache.finish:
            taches_termined.append(tache)
        else:
            taches_no_termined.append(tache)
    form = tachesForm()
    if request.method == "POST":
        form = tachesForm(request.POST)
        if form.is_valid():
            form.save()
            form = tachesForm()
        else:
            return render(request, 'index.html', {"form":form,"taches_termined":taches_termined,"taches_no_termined":taches_no_termined})
    else:
        form = tachesForm()
        return render(request, 'index.html', {"form":form,"taches_termined":taches_termined,"taches_no_termined":taches_no_termined})
    return render(request, 'index.html', {"form":form,"taches_termined":taches_termined,"taches_no_termined":taches_no_termined})

# chat gpt

def changer_etat_element(request):

    if request.method == 'POST':
        element_id = request.POST.get('element_id')
        is_checked = request.POST.get('is_checked') == "true"
        date = request.POST.get('date')
        element = Taches.objects.get(id=element_id)
        element.finish = is_checked
        element.finish_duration = date
        element.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

taches = Taches.objects.all()
def modify_task(request,id,taches=taches):
    taches_termined = []
    taches_no_termined = []
    for tache in taches:
        if tache.finish:
            taches_termined.append(tache)
        else:
            taches_no_termined.append(tache)
    obj  = get_object_or_404(Taches,id=id)
    form = tachesForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = tachesForm()
        return redirect("/")
    return render (request,'index.html', {'form':form ,"taches_termined":taches_termined,"taches_no_termined":taches_no_termined})
def delete_task(request,id):
    taches = Taches.objects.all()
    obj = get_object_or_404(Taches,id=id)
    obj = Taches.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        form = tachesForm()
        return redirect('/')
    return render (request,"delete.html",{"obj":obj})
