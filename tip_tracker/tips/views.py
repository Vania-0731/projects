from django.shortcuts import render
from .models import Tip

def tip_list(request):
    tips = Tip.objects.all()
    total = sum(tip.amount for tip in tips)
    return render(request, 'tips/tip_list.html', {'tips': tips, 'total': total})

# Create your views here.
