from django import forms

class BattleShipForm(forms.Form):
	x = forms.IntegerField(label='X Coordinate')
	y = forms.IntegerField(label='Y Coordinate')
