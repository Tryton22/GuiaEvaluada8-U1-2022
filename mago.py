class Wizard():
	def __init__(self):
		self._vulnerable1 = 0
		
	def Esvulnerable(self):
		if self._vulnerable1 == 1:
			return False
		else:
			return True
	
	def Preparahechizo(self):
		self._vulnerable1 = 1
		return self._vulnerable1
	
	def Damage(self):
		if self._vulnerable1 == 0:
			return "El guerrero pego 10 puntos."
		else:
			return "El guerrero pego 6 puntos."
 
