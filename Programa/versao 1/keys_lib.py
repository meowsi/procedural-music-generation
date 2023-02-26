from music21 import *

# Cada tom possui diferentes modos, cada um com uma escala de sete notas
# Algumas notas são comuns a todos os modos, outras não

class Do:
	def __init__(self, modo):
		self.do = note.Note("C4")
		self.re = note.Note("D4")
		self.fa = note.Note("F4")
		self.sol = note.Note("G4")
		
		if modo == 'menor natural':
			self.mi = note.Note("E-4")
			self.la = note.Note("A-4")
			self.si = note.Note("B-4")

		elif modo == 'maior natural':
			self.mi = note.Note("E4")
			self.la = note.Note("A4")
			self.si = note.Note("B4")

		self.do.array_pesos = [0.1, 0.45, 0.2, 0.1, 0.07, 0.05, 0.03]
		self.re.array_pesos = [0.03, 0.1, 0.45, 0.2, 0.1, 0.07, 0.05]
		self.mi.array_pesos = [0.05, 0.03, 0.1, 0.45, 0.2, 0.1, 0.07]
		self.fa.array_pesos = [0.07, 0.05, 0.03, 0.1, 0.45, 0.2, 0.1]
		self.sol.array_pesos = [0.1, 0.07, 0.05, 0.03, 0.1, 0.45, 0.2]
		self.la.array_pesos = [0.2, 0.1, 0.07, 0.05, 0.03, 0.1, 0.45]
		self.si.array_pesos = [0.45, 0.2, 0.1, 0.07, 0.05, 0.03, 0.1]

		self.escala = [self.do, self.re, self.mi, self.fa, self.sol, self.la, self.si]

class Re:
	def __init__(self, modo):
		self.re = note.Note("D4")
		self.mi = note.Note("E4")
		self.sol = note.Note("G4")
		self.la = note.Note("A4")
		
		if modo == 'menor natural':	
			self.fa = note.Note("F4")
			self.si = note.Note("B-4")
			self.do = note.Note("C4")
		
		if modo == 'maior natural':
			self.fa = note.Note("F#4")
			self.si = note.Note("B4")
			self.do = note.Note("C#4")

		self.re.array_pesos = [0.1, 0.45, 0.2, 0.1, 0.07, 0.05, 0.03]
		self.mi.array_pesos = [0.03, 0.1, 0.45, 0.2, 0.1, 0.07, 0.05]
		self.fa.array_pesos = [0.05, 0.03, 0.1, 0.45, 0.2, 0.1, 0.07]
		self.sol.array_pesos = [0.07, 0.05, 0.03, 0.1, 0.45, 0.2, 0.1]
		self.la.array_pesos = [0.1, 0.07, 0.05, 0.03, 0.1, 0.45, 0.2]
		self.si.array_pesos = [0.2, 0.1, 0.07, 0.05, 0.03, 0.1, 0.45]
		self.do.array_pesos = [0.45, 0.2, 0.1, 0.07, 0.05, 0.03, 0.1]

		self.escala = [self.re, self.mi, self.fa, self.sol, self.la, self.si, self.do]

