from mago import Wizard
class Warrior(Wizard):
	def __init__(self):
		super().__init__()
		self._vulnerable = 1
		
	def Isvulnerable(self):
		if self._vulnerable == 1:
			return False
			
	def Damage1(self):
		if self._vulnerable1 == 1:
			return "El mago pego 12 puntos."
		else:
			return "El mago pego 3 puntos."
			

