from common_imports import *
import settings

# Cada tom possui diferentes modos, cada um com uma escala de catorze notas (duas oitavas)
# Algumas notas são comuns a todos os modos, outras não

class C:
	def __init__(self, modo):
		self._1 = note.Note("C4")
		self._2 = note.Note("D4")
		self._4 = note.Note("F4")
		self._5 = note.Note("G4")

		self._8 = note.Note("C5")
		self._9 = note.Note("D5")
		self._11 = note.Note("F5")
		self._12 = note.Note("G5")
		
		if modo == 'menor natural':
			self._3 = note.Note("E-4")
			self._6 = note.Note("A-4")
			self._7 = note.Note("B-4")

			self._10 = note.Note("E-5")
			self._13 = note.Note("A-5")
			self._14 = note.Note("B-5")

			self.ks = -3

		elif modo == 'maior natural':
			self._3 = note.Note("E4")
			self._6 = note.Note("A4")
			self._7 = note.Note("B4")

			self._10 = note.Note("E5")
			self._13 = note.Note("A5")
			self._14 = note.Note("B5")

			self.ks = 0
			
		settings.setKeyScale(self)
		settings.setNoteScales(self)
		settings.setChords(self)