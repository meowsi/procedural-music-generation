from music21 import *
import settings

# Cada tom possui diferentes modos, cada um com uma escala de catorze notas (duas oitavas)
# Algumas notas são comuns a todos os modos, outras não

class C_key:
	def __init__(self, modo):
		self._1 = note.Note("C4")
		self._2 = note.Note("D4")
		self._4 = note.Note("F4")
		self._5 = note.Note("G4")

		self._1up = note.Note("C5")
		self._2up = note.Note("D5")
		self._4up = note.Note("F5")
		self._5up = note.Note("G5")
		
		if modo == 'menor natural':
			self._3 = note.Note("E-4")
			self._6 = note.Note("A-4")
			self._7 = note.Note("B-4")

			self._3up = note.Note("E-5")
			self._6up = note.Note("A-5")
			self._7up = note.Note("B-5")

		elif modo == 'maior natural':
			self._3 = note.Note("E4")
			self._6 = note.Note("A4")
			self._7 = note.Note("B4")

			self._3up = note.Note("E5")
			self._6up = note.Note("A5")
			self._7up = note.Note("B5")

		settings.setScales(self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._1up, self._2up, self._3up, self._4up, self._5up, self._6up, self._7up)
		
		
class D_key:
	def __init__(self, modo):
		self._1 = note.Note("D4")
		self._2 = note.Note("E4")
		self._4 = note.Note("G4")
		self._5 = note.Note("A4")

		self._1up = note.Note("D5")
		self._2up = note.Note("E5")
		self._4up = note.Note("G5")
		self._5up = note.Note("A5")
		
		if modo == 'menor natural':	
			self._3 = note.Note("F4")
			self._6 = note.Note("B-4")
			self._7 = note.Note("C5")

			self._3up = note.Note("F5")
			self._6up = note.Note("B-5")
			self._7up = note.Note("C6")
		
		if modo == 'maior natural':
			self._3 = note.Note("F#4")
			self._6 = note.Note("B4")
			self._7 = note.Note("C#5")

			self._3up = note.Note("F#5")
			self._6up = note.Note("B5")
			self._7up = note.Note("C#6")

		settings.setScales(self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._1up, self._2up, self._3up, self._4up, self._5up, self._6up, self._7up)
