from django.shortcuts import render
from .models import Hero

def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'heroes/hero_list.html', {'heroes':heroes})
# Create your views here
# .
