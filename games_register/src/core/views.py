from django.shortcuts import render
from .models import VideoGame

def game_list(request):
    games = VideoGame.objects.all()
    return render(request, 'core/game_list.html',{'games': games})

# Create your views here.
