from django.shortcuts import render
from django.http import HttpResponse, Http404

from utils.battleship import BattleShip
from forms import BattleShipForm

def home(request):
	b = BattleShip()
	b.add_random_ships(3)

	if request.method == 'POST':
		f = BattleShipForm(request.POST)
		if f.is_valid():
			x = request.POST.get('x')
			y = request.POST.get('y')
			return render(request, 'battleship/index.html', {'ocean': b.ocean, 'message': x + ' x ' + y })
	else:
		f = BattleShipForm()
	return render(request, 'battleship/index.html', {'ocean': b.ocean , 'form': f})
