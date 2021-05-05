from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse


# Create your views here.
def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def create(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('superhero_name')
        alter_ego = request.POST.get('alter_ego')
        name = request.POST.get('name')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego=alter_ego, name=name,
                                  primary_ability=primary_ability, secondary_ability=secondary_ability,
                                  catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')
